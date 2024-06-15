import os
import sys
os.chdir("/home/wdy/code_LLM/FL_research")
sys.path.append("/home/wdy/code_LLM/FL_research")

import io
import re
import json
import copy
import uuid
import time
import difflib
import logging
import difflib
import pandas as pd
import gradio as gr
import xml.etree.ElementTree as ET
from logging import Logger
from typing import Optional
from implement.exceptions import *

## 全局
DEMO_CODE_FOLDER = 'static/data'
ERROR_TYPE_FILE = 'static/data/error_type.xlsx'
PATH_019 = "static/student/019-学生名册.xlsx"
PATH_018 = "static/student/018-学生名册.xlsx"
PATH_015 = "static/student/015-学生名册.xlsx"

## 基础类
class TestCasesLoader:
    """
        Load test cases from folder, in which xml-style files exists.\n
        Return: 
         - Dict[str(id):(list[input], list[output])]
    """
    def __init__(self, test_cases_folder_path: str):     
        self.test_cases_folder_path = test_cases_folder_path   
    
    def xml2json(self, xml_path: str) -> dict:
        # 解析 XML 文件
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # 递归函数，将 Element 对象转换为字典
        def element_to_dict(element):
            result = {}
            if element.attrib:
                result.update(element.attrib)
            if element.text:
                result[element.tag] = element.text
            for child in element:
                child_dict = element_to_dict(child)
                result.setdefault(child.tag, []).append(child_dict)
            return result

        # 将根节点转换为字典
        json_data = element_to_dict(root)
        return json_data

    def parse_dict(self, dic: dict) -> tuple:
        count = int(dic['count'])
        inputs = []
        outputs = []
        for i in range(count):
            case_name = 'testData' + str(i + 1)
            inputs.append(dic[case_name][0]['input'][0]['input'])
            outputs.append(dic[case_name][0]['output'][0]['output'])
        return inputs, outputs

    def get_test_cases(self) -> dict:
        test_cases_name = os.listdir(self.test_cases_folder_path)

        return {
            os.path.splitext(name)[0][-4:]:
            self.parse_dict(
                self.xml2json(
                    os.path.join(self.test_cases_folder_path, name)
                )
            ) for name in test_cases_name if name.endswith('.xml')
        }

class Mylogger(Logger):
    """
    Customized Logger.
    """
    def __init__(self, session_manager=None, log_file_name='log_dev', level=logging.DEBUG):
        super().__init__('my_logger', level=level)
        formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # 设置日志格式
        fh = logging.FileHandler(log_file_name)  # 创建一个文件句柄，用于将日志记录保存到文件
        fh.setFormatter(formater)  # 设置文件句柄的日志格式
        
        self.addHandler(fh)
        self.session_manager = session_manager
        self.__mete_data__ = {
            'msg_type': None, 'user': None, 'prob_input': None, 'code_input': None, 
            'prob_id': None, 'fix_suggestion': None, 'is_like': None, 'feedback': None, 
            'dialogue': None, 'err_info': None, 'traceback_info': None
        }
        
        self.meta_data = copy.deepcopy(self.__mete_data__)

    def __getitem__(self, key):
        return self.meta_data[key]
    
    def __setitem__(self, key, value):
        self.meta_data[key] = value
    
    def logger_info_render(self, req: gr.Request, msg: dict=None):
        # extra msg to add
        if msg:            
            self.meta_data.update(msg)
        
        # update current user
        self.meta_data['user'] = self.session_manager.get_current_user(req)
     
        return json.dumps(self.meta_data, ensure_ascii=False, indent=4)

    def info(self, req: gr.Request, msg: dict=None) -> None:
        super().info(self.logger_info_render(req, msg))
        self.clear_meta_data()
    
    def error(self, req: gr.Request, msg: dict=None) -> None:
        super().error(self.logger_info_render(req, msg))
        self.clear_meta_data()
        
    def clear_meta_data(self,):
        self.meta_data = copy.deepcopy(self.__mete_data__)

class SessionManager:
    """
    Use to manage the current login user.
    """
    def __init__(self):
        self.sessions = {}
        self.current_session_id = None

    def get_current_user(self, req: gr.Request):
        for user, session_list in self.sessions.items():
            if user == req.username:
                return user
        return "No user logged in with this username"

    def get_user(self, req: gr.Request):
        """
            gr.Request: \n
            A Gradio request object that can be used to access the request headers, cookies, \
            query parameters and other information about the request;\n
            If auth is enabled, the username attribute can be used to get the logged in user.
        """
        session_id = str(uuid.uuid4())
        timestamp = time.time()
        if req.username not in self.sessions:
            self.sessions[req.username] = [(session_id, timestamp)]
        else:
            self.sessions[req.username].append((session_id, timestamp))
            self.sessions[req.username].sort(key=lambda x: x[1]) # sort by timestamp
            if len(self.sessions[req.username]) > 5:
                self.sessions[req.username].pop(0) # remove the oldest sessions
        current_user = self.get_current_user(req)
        return gr.Markdown(value=f"您好！ {current_user}，欢迎使用本系统")

## sbfl工具类和函数
class CustomStdout(io.TextIOWrapper):
    def __init__(self, buffer) -> None:
        super().__init__(buffer)
        self.tmp_output_str = ''
        # self.logger = logger
    
    def write(self, __s: str) -> int:        
        self.tmp_output_str += __s
        # try:
        #     return super().write(str(__s))
        # except TypeError:
        #     raise BytesWriteError
    
    def erase(self):
        self.tmp_output_str = ''

def coverage_vec_transformer(cov_info: str, total_line: int, file_name: str) -> list[bool]:
    """
        parse the json_report generated by coverage.py, and return cov_vector in sbfl-style.
    """

    info = json.loads(cov_info)
    cov_vec = [0] * total_line
    executed_lines = info['files'][file_name]['executed_lines']
    total_code_line = info['files'][file_name]['summary']['num_statements']
    
    for x in executed_lines:
        cov_vec[x - 1] = 1

    return cov_vec, total_code_line

def get_target_lines_span(lst: list[int]) -> str:
    """
        get the span of target lines
    """
    if not lst:
        return []
    slices = []
    start = lst[0]
    end = lst[0]

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            end = lst[i]
        else:
            if start == end:
                slices.append(f"line{start}")
            else:
                slices.append(f"line{start}~{end}")
            start = lst[i]
            end = lst[i]

    if start == end:
        slices.append(f"line{start}")
    else:
        slices.append(f"line{start}~{end}")

    res = '\n\n'.join(slices)
    return res

def get_type(testcase_output: str) -> type:
    '''
    判断测试用例实际数据类型
    '''
    try:
        value = eval(testcase_output)
        return type(value)
    except (SyntaxError, NameError):
        return str

## 字符串处理函数    
def find_words(str_index: int, testcase_output: str) -> list:
    # 找出缺失字符处前后的单词 
    pre_word = ""
    post_word = ""
    # 处理边界情况：如果索引小于0或大于等于字符串长度，则直接返回空列表
    if str_index <= 0:
        post_word = testcase_output.split()[0]
        return pre_word, post_word
    elif str_index >= len(testcase_output):
        pre_word = testcase_output.split()[-1]
        return pre_word, post_word

    # 向前搜索找到前一个单词的起始位置
    pre_index = str_index
    while pre_index >= 0 and testcase_output[pre_index] != ' ':
        pre_index -= 1
    # 向后搜索找到后一个单词的起始位置
    post_index = str_index
    while post_index < len(testcase_output) and testcase_output[post_index] != ' ':
        post_index += 1

    # 处理其他位置的情况
    pre_index -= 1
    post_index += 1
    while pre_index >= 0 and testcase_output[pre_index] != " ":
            pre_word = testcase_output[pre_index] + pre_word
            pre_index -= 1
    while post_index < len(testcase_output) and testcase_output[post_index] != " ":
            post_word += testcase_output[post_index]
            post_index += 1

    return pre_word, post_word

def match_print(output: str, testcase_output: str) -> Optional[str]:
    if get_type(testcase_output) == str:
        # 使用 difflib 模块找出差异
        differ = difflib.ndiff(testcase_output, output)
        
        # 构建字符差别列表，其中diff[0]表示是'+'或'-',diff[2]表示差异的字符
        differences = [(i, diff[0], diff[2]) for i, diff in enumerate(differ) if diff[0] != ' ']
    
        if differences:
            miss_string = f"你输出的字符串为:\n{output}\n与标准答案相比,"
            for i,diff_mark,diff_word in differences:
                # print(i)
                if diff_word == ' ':
                    char = "空格"
                else:
                    char = diff_word

                pre_word, post_word = find_words(i, testcase_output)
                if pre_word == "" or post_word == "":

                    if pre_word == "":
                        if diff_mark == '+':
                            miss_string += f"在{post_word}之前的位置存在多了'{char}'的问题,"
                        elif diff_mark == '-':
                            miss_string += f"在{post_word}之前的位置存在少了'{char}'的问题,"
                    elif post_word == "":
                        if diff_mark == '+':
                            miss_string += f"在{pre_word}之后的位置存在多了'{char}'的问题,"
                        elif diff_mark == '-':
                            miss_string += f"在{pre_word}之后的位置存在少了'{char}'的问题,"

                else:
                    if diff_mark == '+':
                        miss_string = miss_string + f"在{pre_word}和{post_word}之间的位置存在多了'{char}'的问题,"
                    elif diff_mark == '-':
                        miss_string = miss_string + f"在{pre_word}和{post_word}之间的位置存在少了'{char}'的问题,"

            return miss_string[:-1] # 去除字符串中最后一个逗号
    return None

def check_input_args(code):
    """
    判断输入的代码中是否有 input 函数调用有参数
    """
    input_pattern = r'\binput\s*\(\s*[^)]+\s*\)'
    return bool(re.search(input_pattern, code))

def find_json_positions(input_string):
    """
    在输入字符串中查找 JSON 格式的子串，并返回它们的位置
    """
    positions = []
    stack = []
    start = None

    for i, char in enumerate(input_string):
        if char == '{':
            if not stack:
                start = i
            stack.append(char)
        elif char == '}':
            if stack:
                stack.pop()
                if not stack:
                    positions.append((start, i + 1))
            else:
                start = None

    return positions

def analysis_res_format(res: list, FL_text: str):
    intendent = '  '
    res_ = None
    
    def format_dict_1(d):
        """
        format dict like: {1:[[], []], 2:[[]]}
        """
        result = "{\n"
        for key, value in d.items():
            result += "  " + repr(key) + ": [\n"
            for item in value:
                result += "    " + repr(item) + ",\n"
            result += "  ],\n"
        result += "}"
        return result
    
    def dict_format_2(touple: dict):
        """
        format dict like: {3: {'f': [0, 0, 0, 0, 0], 'p': [0, 0, 0, 0, 0]}}}
        """
        intendent = '  '
        ans = '\n{\n'
        for k, v in touple.items():
            ans += f"{intendent + str(k)}: {'{'}\n"
            for k1, v1 in v.items():
                ans += f'{intendent + intendent + str(k1)}: {str(v1)},\n'
            ans += f'{intendent + "}"}\n'
        ans += '}'
        return ans
    
    if FL_text == 'mbfl':
        res_ = [0] * 5
        # res: ((ori_cov_info, out_dict), (mut_complile_info, sus_list_sort), touple, target_lines)
        # (ori_cov_info, out_dict): ([[], [], ...], []), {1:[[], []], 2:[[]]}
        res_[0] = 'cov_mat: \n[\n' + '\n'.join([intendent + str(x) for x in res[0][0][0]]) + '\n]' + \
                    '\npass_vec: \n' + str(res[0][0][1]) + \
                    f'\n\nout_dict:\n{format_dict_1(res[0][1])}'
        # (mut_complile_info, sus_list_sort): (muts_num, compile_mut_num, sus_list_sort)
        res_[1] = f'muts_num: {res[1][0]}\ncompile_mut_num: {res[1][1]}'
        # touple: {'tf': 5, 'tp': 0, 'f2p': 0, 'p2f': 0, 'f&p': {3: {'f': [0, 0, 0, 0, 0], 'p': [0, 0, 0, 0, 0]}}}     
        res_[2] = f'tf: {res[2]["tf"]}\ntp: {res[2]["tp"]}\nf2p: {res[2]["f2p"]}\np2f: {res[2]["p2f"]}\nf&p: ' + \
                    dict_format_2(res[2]["f&p"])
        # sus_list_sort: [[4, -1.0], [5, -1.0], [6, -1.0], [7, -1.0], [8, -1.0], [9, -1.0], [12, -1.0]]
        res_[3] = '[\n' + '\n'.join([intendent + str(x) for x in res[1][2]]) + '\n]'
        # target_lines
        # res_[4] = get_target_lines_span(res[3])
        res_[4] = res[3]
    else:
        res_ = [0] * 4
        # res: (cov_info, line_rank, ([stu_output], [gold_output]), target_lines:())
        # cov_info: (cov_mat, pass_vec)
        res_[0] = f'cov_mat: \n[\n' + '\n'.join([intendent + str(x) for x in res[0][0]]) + '\n]\n' + \
            f'\npass_vec: \n{res[0][1]}'
        # line_rank
        res_[1] = f'line_rank: \n{res[1]}'
        # ([stu_output], [gold_output])
        res_[2] = f'\nstu_output: \n{res[2][0]}\ngold_output: \n{res[2][1]}\n'
        # target_lines
        res_[3] = res[3]
    return res_
    
## 编译错误工具函数
def map_(input_text):
    #输入文本
    # input_text = "TypeError: unsupported operand type(s) for ^: 'int' and 'float'"
    demo_code_folder = DEMO_CODE_FOLDER

    errorType = pd.read_excel(ERROR_TYPE_FILE)
    type = []
    for i in range(len(errorType)):
        information = {
            'num': int(errorType['number'][i]),
            'type': errorType['type'][i],
            'context': errorType['context'][i]
        }
        type.append(information)

    # 计算输入文本与预设错误类型文本信息的相似度
    best_match = None
    global best_similarity
    best_similarity = 0
    for info in type:
        similarity = difflib.SequenceMatcher(None, input_text, info['type']).ratio()
        if similarity > best_similarity:
            # 相似度的数据需要被收集
            best_similarity = similarity
            best_match = info

    # 输出相似度最高的文本信息及示例代码 
    if best_similarity > 0.4:
        code_file_name = str(best_match['num']) + ".py"
        code_file_path = os.path.join(demo_code_folder, code_file_name)
        # 检查示例代码文件是否存在
        if os.path.exists(code_file_path):
            # 读取示例代码内容
            with open(code_file_path, "r") as file:
                code = file.read()
            return f"**存在的错误**：\n\n{best_match['context']}\n\n" + f"\n\n**示例代码：**\n\n```ss\n{code}\n"
        else:
            return "未找到对应的示例代码文件"
    else:
        return "本系统暂时无法处理该错误，请您咨询助教，老师或其他检索方法解决该问题!"

class ProbIdTransformer:
    def __init__(self, prob2id_folder) -> None:
        text2id = pd.read_excel(os.path.join(prob2id_folder, 'problem_text2id.xlsx'))
        text_cut = pd.read_excel(os.path.join(prob2id_folder,'problem_cut.xlsx'))
        
        # Completion problems
        self.cut_ids = []

        # all problems
        self.text = {str(text2id['id'][i]): text2id['text'][i] for i in range(len(text2id))}
        for i in range(len(text_cut)):
            self.text.update({str(text_cut['id'][i]): text_cut['text'][i]})
            self.cut_ids.append(str(text_cut['id'][i]))
            
    def problem_text2id(self, input_text):
        # 计算输入文本与预设问题描述文本信息的相似度
        best_match = None
        best_similarity = 0

        for id_, text in self.text.items():
            similarity = difflib.SequenceMatcher(None, input_text, text).ratio()
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = id_

        # match nothing
        if not best_match or best_similarity < 0.4:
            raise ProbNotIncludedError
        
        # return only the id not in cut_ids
        return best_match if best_match not in self.cut_ids else 0
    
    def id2problem_text(self, id_to_find: str):
        try:
            return self.text[id_to_find]
        except KeyError:
            return "pron2id映射表未导入此id"
        except Exception as e:
            return f"发生错误：{e}"

def student():
    path_019 = PATH_019
    path_018 = PATH_018
    path_015 = PATH_015

    student_data_019 = pd.DataFrame(pd.read_excel(path_019))
    student_data_018 = pd.DataFrame(pd.read_excel(path_018))
    student_data_015 = pd.DataFrame(pd.read_excel(path_015))

    student_019 = list(student_data_019[['姓名', '学号']].apply(tuple, axis=1))
    student_018 = list(student_data_018[['姓名', '学号']].apply(tuple, axis=1))
    student_015 = list(student_data_015[['姓名', '学号']].apply(tuple, axis=1))

    student = student_019+student_018+student_015
    for i in range(len(student)):
        password = student[i][1]
        student[i] = (student[i][0], str(password))

    return student


if __name__ == '__main__':
    # 示例用法
    
    res = (1, ([[1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 0]], [1, 0, 0, 0, 0]),
           2, {'tf': 5, 'tp': 0, 'f2p': 2, 'p2f': 0, 'f&p': {1: {'f': [0, 0], 'p': [0, 0]}, 2: {'f': [0, 1, 1], 'p': [0, 0, 0]}, 6: {'f': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'p': [0, 0, 0, 0, 0, 0, 0, 0, 0]}, 8: {'f': [0, 0, 0, 0, 0, 0, 0, 0, 0], 'p': [0, 0, 0, 0, 0, 0, 0, 0, 0]}}}
           , [[4, -1.0], [5, -1.0], [6, -1.0], [7, -1.0], [8, -1.0], [9, -1.0], [12, -1.0]])
    intendent = '  '
    # def dict_format(touple: dict):
    #     
    #     ans = '\n{\n'
    #     for k, v in touple.items():
    #         ans += f"{intendent + str(k)}: {'{'}\n"
    #         for k1, v1 in v.items():
    #             ans += f'{intendent + intendent + str(k1)}: {str(v1)},\n'
    #         ans += f'{intendent + "}"}\n'
    #     ans += '}'
    #     return ans
                
    # res[3] = f'tf: {res[3]["tf"]}\ntp: {res[3]["tp"]}\nf2p: {res[3]["f2p"]}\np2f: {res[3]["p2f"]}\nf&p: ' + \
    #             dict_format(res[3]["f&p"])
    # print(res[3])
    res[4] = 'cov_mat: \n[\n' + '\n'.join([intendent + str(x) for x in res[4]]) + '\n]'
    print(res[4])
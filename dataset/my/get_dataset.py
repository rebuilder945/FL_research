import io
import os
import sys
import pdb
# os.chdir("/home/wdy/code_LLM/FL_research")
sys.path.append("/home/wdy/code_LLM/FL_research")
from tqdm import tqdm
from implement.techs import *
from implement.utils import *
from dataset.my.utils import *

class StuDataset:
    def __init__(self, ori_data_path: str, tar_data_path: str):
        self.dataset = []
        # step1: get last2list
        print('step1: get last2list...')
        last2list = get_last2list(ori_data_path) # [(prob_id_, last2, last1)...]
        # step2: filter and copy
        print('step2: filter and copy...')
        folder_check(tar_data_path)
        for index, (prob_id, fl2, fl1) in tqdm(enumerate(last2list), total=len(last2list)):
            name, prob_id_ = prob_id.split("-")
            with open(os.path.join(ori_data_path, fl2), "r")as f2, \
                  open(os.path.join(ori_data_path, fl1), "r") as f1:                
                code_fl2 = f2.read()
                code_fl1 = f1.read()
            # run res filter: 0: cut, 1: pass, -1: fail, 2: compile error                  
            res_flag_2 = FL_app.analysis(code_fl2, prob_id_, fl2)
            res_flag_1 = FL_app.analysis(code_fl1, prob_id_, fl1)
            
            # TODO：有些代码（如下两个）这样批量执行会被跳过，暂时无法解决
            # if prob_id == '俞锡凯-2999' or prob_id == '郭大远-2999':
            #     if not (res_flag_2 == -1 and res_flag_1 == 1):
            #         print(prob_id, fl2, fl1)
            #         pdb.set_trace()
            if res_flag_2 == -1 and res_flag_1 == 1:
                # diff line filter: diff_line_num: int, false
                res_diff_line = compare_code(code_fl2, code_fl1)
                if res_diff_line:
                    self.dataset.append((prob_id_, fl2, fl1))
                    # mkdir                    
                    folder_check(os.path.join(tar_data_path, prob_id_))
                    tar_name_path = os.path.join(tar_data_path, prob_id_, name)
                    folder_check(tar_name_path)
                    # copy
                    shutil.copyfile(
                        os.path.join(ori_data_path, fl2),
                        os.path.join(tar_name_path, 'false.py')
                    )
                    shutil.copyfile(
                        os.path.join(ori_data_path, fl1),
                        os.path.join(tar_name_path, 'true.py')
                    )
                    with open(os.path.join(tar_name_path, f"{res_diff_line}.txt"), "w"):
                        pass
        print(f'labeled dataset: {len(self.dataset) * 2}')
    
    def get_len(self):
        return len(self.dataset) * 2
    
    def get_dataset(self, index):
        return self.dataset


def get_excel(dataset_path: str, report_path: str):
    # 获取dataset/val/val_c4_5_17.xlsx，即对于dataset/ch4_labeled的sbfl和mbfl分析
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(
        ["prob_id", "cases_txt"]
        + FL_app.headers['mbfl']
        + ['delimiter']
        + FL_app.headers['sbfl']
        + ['code_f', 'code_t']
        + ['mbfl_target_lines']
        + ['sbfl_target_lines']
        + ['label_lines']
    )
    
    # acc cal
    total_code = 94
    mbfl_acc = sbfl_acc = 0
    ori_data = os.listdir(dataset_path)
    for prob_id_ in tqdm(ori_data, total=len(ori_data)):
        prob_path = os.path.join(dataset_path, prob_id_)        
        cases_txt = "".join(
            [
                f"test{index + 1}:\ninput:\n{x}output:\n{y}\n\n"
                for index, (x, y) in enumerate(
                    zip(FL_app.test_cases[prob_id_][0], FL_app.test_cases[prob_id_][1])
                )
            ]
        )        
        for name in os.listdir(prob_path):
            name_path = os.path.join(prob_path, name) 
            f_f = open(os.path.join(name_path, 'false.py'), 'r').read() # 错误代码
            t_f = open(os.path.join(name_path, 'true.py'), 'r').read() # 正确代码
            prob_id = name + '-' + prob_id_ # 代码标识
            # label错误行
            label_line = int([x for x in os.listdir(name_path) if x.endswith('.txt')][0][:-4])

            # 执行分析
            # 传统方法
            res_mbfl, res_sbfl = FL_app.analysis_(code_=f_f, prob_id=prob_id_, stu=prob_id)
            mbfl_tar_l = res_mbfl[-1] # list
            sbfl_tar_l = res_sbfl[-1] # list
            # chatgpt
            gpt_res = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        # "content": "下面给你一道编程题，题目是：“读入一个自然数构成的列表，找出其中的每一个素数，"+ \
                        #     "然后放入另外一个列表，并输出这个列表。”，接下来我会给你一段对代码行顺序行进行编号后的python代码，" + \
                        #     "请你直接说出第几行有错误，并说出为什么。",
                        "content": f"""
Please analyse the following code snippet for potential bugs. The code is written to solve the code problem:
{prob_text}
You need to return the results in JSON format, consisting of a single JSON object with two fields: 
"intentOfThisCode" (describing the intended purpose of the code), and "faultLocalization" (an array of JSON objects). 
The "faultLocalization" array should contain only one JSON object which you think is the most suspicious buggy line with three fields: 
"lineNumber" (indicating the line number of the suspicious code), "codeContent" (showing the actual code), 
and "reason" (explaining why this location is identified as potentially faulty). 
Note: The codes in the "faultLocalization" array should be listed in descending order of suspicion
""",
                    },
                    {
                        "role": "user",
                        "content": code_,
                    },
                ],
            )
            

            # 统计准确性
            if mbfl_tar_l != '//':
                if len(mbfl_tar_l) == 1 and label_line in mbfl_tar_l:
                    mbfl_acc += 1
            if sbfl_tar_l != '//':
                if len(sbfl_tar_l) == 1 and label_line in sbfl_tar_l:
                    sbfl_acc += 1

            # 加入excel行
            ws.append(
                [prob_id, cases_txt]    
                + res_mbfl[:-1]
                + ['delimiter']
                + res_sbfl[:-1]
                + [f_f, t_f]
                + [str(res_mbfl[-1])]
                + [str(res_sbfl[-1])]
                + [str(label_line)]
            )

    print(f"mbfl acc: {mbfl_acc}/{total_code}, sbfl acc: {sbfl_acc}/{total_code}")

    # 保存结果
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(wrapText=True)
    wb.save(report_path)


if __name__ == "__main__":
    # code analysis
#     code_ = """a=int(input())
# b=int(input())
# if a > b:
#     print(a)
# else:
#     print(a)"""
#     testcase = (["7\n8", "57\n50", "57\n60"], ["8", "57", "60"])

    # analyze
    log_file_name = "tmp/logs/log_analysis_dataset"
    test_cases_folder_path = "static/data/testcase"
    prob2id_folder = "static/prob2id_map"

    session_manager = SessionManager()
    logger = Mylogger(session_manager, log_file_name)
    prob2ider = ProbIdTransformer(prob2id_folder)
    test_cases = TestCasesLoader(test_cases_folder_path).get_test_cases()
    alg_mbfl = MBFL(cov=Coverage(), my_stdout=CustomStdout(sys.__stdout__), text='mbfl')
    alg_sbfl = SBFL(cov=Coverage(), my_stdout=CustomStdout(sys.__stdout__), text='sbfl')

    FL_app = FaultLoalization(
        test_cases=test_cases,
        logger=logger,
        algorithm=alg_sbfl,
    )
    

    dataset = StuDataset(
        # ori_data_path=r'analysis/code_filter/chapter4',
        # ori_data_path=r'/data/code-data/student_code_chapter5',
        ori_data_path=r'/data/code-data/student_code_chapter6',
        tar_data_path=f'dataset/test/ch6_labeled'
    )

    # get_excel(
    #     dataset_path="dataset/ch4_labeled",
    #     report_path="dataset/val/val_c4_5_17.xlsx",
    # )

    # FL_app.analysis(
    #     dataset_path="dataset/val/val_",
    #     report_path="dataset/val/val_c4_true.xlsx",
    # )


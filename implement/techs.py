import io
import os
import sys
os.chdir("/home/wdy/code_LLM/FL_research")
sys.path.append("/home/wdy/code_LLM/FL_research")
import signal
import shutil
import numpy as np
import sbfl.base
import DNMBFL.mbfl.command as mbfl
import DNMBFL.mbfl.mbfl_for as mbfl_for

from tqdm import tqdm
from openai import OpenAI
from logging import Logger
from coverage import Coverage
from implement.utils import *
from unittest.mock import patch
from implement.exceptions import *
from openpyxl.styles import Alignment
from contextlib import contextmanager
from sbfl.base import SBFL as sbfl_cal

# 设置定时器，检测代码是否死循环
def timeout_handler(signum, frame):
    raise TimeoutException
signal.signal(signal.SIGALRM, timeout_handler)

# logger
chapter = 4
logger_ = Logger('my_logger', logging.INFO)
fh = logging.FileHandler(f'analysis_log_c{chapter}')  # 创建一个文件句柄，用于将日志记录保存到文件
logger_.addHandler(fh)

# chatgpt api
client = OpenAI(
    api_key=r'sk-nrflxbcRZIXY6dUy40Ea26F13d0d4d5e8632C4D045C0642b',
    base_url=r'https://free.gpt.ge/v1/',
    default_headers={"x-foo": "true"}
)


class FL_alg:
    """
    - split_cha: the split character of every element of test_cases input
    """
    def __init__(self, cov: Coverage, my_stdout: io.TextIOWrapper, text: str) -> None:
        self.text = text
        self.cov = cov
        self.my_stdout = my_stdout
        self.split_cha = "\n"
        self.exce_res = None
        self.total_code_line = 0

    def cal(self, code_: str, test_case: tuple[list], stu: str) -> tuple:
        # test_case[0]: inputs, test_case[0]: outputs
        self.exce_res = self.get_exec_res(code_, test_case, stu)

    def get_exec_res(self, code_: str, test_case: tuple[list], stu: str) -> dict:
        """
        execute the `code_` with `test_case`, return cov_info and outputs_info
        """
        # get total_line of code_file
        total_line = len(code_.split(self.split_cha))

        # create tmp_code.py
        tmp_code_file = "tmp_code.py"
        with open(tmp_code_file, "w", encoding="utf8") as tmp_code:
            tmp_code.write(code_)
        
        # vectors used to cal sbfl
        correct_vec = []
        cov_vecs = []

        # stu_output and test_output
        stu_outputs = []
        gold_outputs = []

        with self.redirect_io():
            for test_input, test_output in zip(test_case[0], test_case[1]):
                # start will reload the data file
                self.cov.start()

                with patch(
                    "builtins.input", side_effect=test_input.split(self.split_cha)
                ):
                    # exec的方式并不能被coverage识别
                    # TODO: tmp_code.py只能放在工作目录，否则：no data report；
                    import tmp_code
                
                # stop collect generate the json_report
                self.cov.stop()
                self.cov.json_report(outfile="-", omit=[__file__, 'implement/utils.py'])  # exclude __file__
                tmp_output_str = self.my_stdout.tmp_output_str
                self.post_process()
                # self.logger_.info(self.my_stdout.tmp_output_str)

                # get stdout info for this test
                split_index = find_json_positions(tmp_output_str)[-1][0]
                
                # TODO
                # logger_.info(f"{stu}-tmp_output_str: {tmp_output_str}")
                
                stu_output = tmp_output_str[:split_index].strip()
                cov_report = tmp_output_str[split_index:].strip()
                

                # self.logger_.info((stu_output, cov_report, test_output))

                stu_outputs.append(stu_output)
                gold_outputs.append(test_output)

                if stu_output == test_output.strip():
                    correct_vec.append(1)
                else:
                    correct_vec.append(0)
                    # 判断是否仅仅格式问题，是的话直接返回提示
                    # format_error = match_print(stu_output, test_output)
                    # if format_error:
                    #     raise FormatError(format_error)

                # cal the vectors used to cal sbfl
                cov_vec, self.total_code_line = coverage_vec_transformer(
                    cov_report, total_line, tmp_code_file
                )
                cov_vecs.append(cov_vec)
                # self.logger_.info((correct_vec, cov_vecs))
        # TODO
        # logger_.info(f"{stu}-sbfl_output-cov_vecs: {cov_vecs}")
        # logger_.info(f"{stu}-sbfl_output-correct_vec: {correct_vec}")
        # logger_.info(f"{stu}-sbfl_output-stu_outputs: {stu_outputs}")
        # logger_.info(f"{stu}-sbfl_output-gold_outputs: {gold_outputs}")

        res = {
            "cov_info": (cov_vecs, correct_vec),
            "outputs_info": (stu_outputs, gold_outputs)
        }
        # print(res)
        return res

    @contextmanager
    def redirect_io(self):
        """
        redirect io stream from sys.__stdout__ to my_stdout, and finally reset.
        """
        try:
            signal.alarm(1)
            sys.stdout = self.my_stdout
            yield
            # 如果yield x，则在使用时可以通过with ... as x: 来使用这个x
        except Exception as e:
            self.post_process()
            raise e
        finally:
            # 返回sys.__stdout__
            signal.alarm(0)
            sys.stdout = sys.__stdout__

    def post_process(
        self,
    ):
        """
        erase will also discard the data file, so multi-measuring without re-start cov will
        stop collect data in next loop
        """
        self.cov.stop()
        self.cov.erase()
        self.my_stdout.erase()

        try:
            del sys.modules["tmp_code"]
        except:
            pass

class SBFL(FL_alg):
    """
    SBFL algorithm class.
    """

    def __init__(self, cov: Coverage, my_stdout: io.TextIOWrapper, text: str) -> None:
        super().__init__(cov, my_stdout, text)

    def cal(self, code_: str, test_case: tuple[list], stu: str) -> tuple:
        super().cal(code_, test_case, stu)  # get self.cov_info: (cov_mat, pass_vec)

        cov_info = self.exce_res["cov_info"]

        # cal sbfl
        X = np.array(cov_info[0], dtype=bool)
        y = np.array(cov_info[1], dtype=bool)
        sbfl_caler = sbfl_cal(formula="Ochiai")
        sbfl_caler.fit_predict(X, y)
        line_rank = sbfl_caler.ranks(method="max")

        # get target lines(block)
        min_rank = min(line_rank)
        target_lines = [index + 1 for index, s in enumerate(line_rank) if s == min_rank]

        # print(total_code_line, target_lines)
        if self.total_code_line == len(target_lines):
            raise FaultLocalizationError(target_lines, self.total_code_line)

        return cov_info, line_rank, self.exce_res["outputs_info"], target_lines

class MBFL(FL_alg):
    """
    MBFL algorithm class.
    """

    def __init__(self, cov: Coverage, my_stdout: io.TextIOWrapper, text: str) -> None:
        super().__init__(cov, my_stdout, text)
    
    def cal(self, code_: str, test_case: tuple[list], stu: str) -> tuple:
        """
        params:
        code_: str,
        test_case: (inputs_list,outputs_list),
        stu: str

        return:
        flag: bool. is the code valid for mbfl FL? 
        ori_cov_info: ((cov_vecs, correct_vec), out_dict)
        compile_pass_info: (len(muts), compile_pass_num, sus_list)
        touple: {'tp': 12, 'tf': 1, ..., 'f&p': {1:[], 2:[], ...}}
        target_lines: [1, 3, 4]
        """
        ## 保存原代码到文件，以对接后面生成变异体的接口
        with open("tmp/tmp_ori_code.py", "w", encoding="utf8") as f:
            f.write(code_)

        ## 获取原代码的执行结果的覆盖信息，其中的异常在上一级处理
        super().cal(code_, test_case)  # get self.exce_res
        cov_mat = self.exce_res["cov_info"][0] # cov_info: (cov_vecs, correct_vec)
        pass_vec = self.exce_res["cov_info"][1]
        # 原代码已完全正确
        if 0 not in pass_vec:
            raise sbfl.base.NoFailingTestError
        
        ## 得到错误测试用例覆盖行: M行
        fail_cov_lines = set() # start from 1
        for index, s in enumerate(pass_vec):
            if s == 0:
                for index_, x in enumerate(cov_mat[index]):
                    if x == 1:
                        fail_cov_lines.add(index_ + 1)
        
        ## 获取变异体生成规则: Q = M * Ki 个
        mut_text = mbfl.Fom().fom_data("", "tmp/tmp_ori_code.py", list(fail_cov_lines))
        if mut_text == "":
            # 无法生成变异规则
            raise MutationFailedError
        muts = list(map(eval, mut_text.strip().split("\n")))
        
        logger_.info(f'{stu}-mut_num: {len(muts)}')
        """
        muts: 
        [
            [[1, "a=int(input())", "a=int(!input())", "(", "(!", 5]],
            [[1, "a=int(input())", "a=int(input(!))", "(", "(!", 11]]
        ]
        """

        ## 开始变异
        compile_pass_num = 0  # 没有编译错误的有效变异体
        out_dic = {}  # 变异体对测试用例的通过情况
        for i, mut in enumerate(muts):  # 执行Q个变异体，获得相应的输出覆盖信息

            # 生成变异体文件
            mut_folder = f"tmp/FOMs/{stu}"
            if not os.path.exists(mut_folder):
                os.mkdir(mut_folder)
            mut_tmp_path = os.path.join(mut_folder, f"mut_code_{i}.py")
           
            if not mbfl.Fom().mutation_build("tmp/tmp_ori_code.py", mut_tmp_path, mut):
                # 生成失败
                continue

            # 执行变异体
            mut_code_ = ""
            with open(mut_tmp_path, "r", encoding="utf8") as mut_tmp:
                mut_code_ = mut_tmp.read()
            try:
                mut_pass_vec = self.get_exec_res(code_=mut_code_, test_case=test_case)[
                    "cov_info"
                ][1]
            except TimeoutException as t_e:
                # 存在死循环
                logger_.info(f'{stu}-mut-exception: {str(t_e)}')
                continue
            except Exception as e:
                # 编译错误
                logger_.info(f'{stu}-mut-exception: {str(e)}')                
                continue
            else:
                compile_pass_num += 1

            # 获取输出信息
            mes = mut[0] # [变异行，变异前代码，变异后代码，变异前符号，变异后符号，变异位置]
            if mes[0] not in out_dic:
                out_dic[mes[0]] = []
            out_dic[mes[0]].append(mut_pass_vec)

        logger_.info(f'{stu}-compile_pass_mut_num: {str(compile_pass_num)}')
        
        # 计算mbfl怀疑度
        if len(out_dic) == 0:
            # out_dic为空，变异体全部编译错误或变异体都生成失败
            raise MutationFailedError
        touple = mbfl.get_toule_lod(pass_vec, out_dic)
        sus_list = []
        for line in touple["f&p"]:
            touple_list = (
                touple["tf"],
                touple["tp"],
                touple["f&p"][line]["f"],
                touple["f&p"][line]["p"],
                touple["f2p"],
                touple["p2f"],
            )
            sus = mbfl_for.metallaxis(touple_list)
            sus_list.append([line, sus])
        sus_list_sort = sorted(sus_list, key=lambda x: x[1], reverse=True)

        # get target 
        target_lines = []
        if len(sus_list_sort) != 0:
            target_lines = [x[0] for x in sus_list_sort if x[1] == sus_list_sort[0][1]]            

        if len(target_lines) == self.total_code_line:
            raise FaultLocalizationError(target_lines, self.total_code_line)
        return (self.exce_res["cov_info"], out_dic), (len(muts), compile_pass_num, sus_list_sort), touple, target_lines

class FaultLoalization:
    """
    FL algorithoms class. Algorithm api invoking and batch code analysis.
    """
    def __init__(
        self,
        test_cases, 
        logger: Logger,
        algorithm: FL_alg,
        # prob_ids: None
    ) -> None:
        self.test_cases = test_cases
        self.logger = logger
        self.algorithm = algorithm
        self.headers = {
            'mbfl': [
                "ori_cov_info",
                "mut_complile_info",
                "touple",
                "sus_list_sort",
            ],
            'sbfl': [           
                "cov_info",
                "line_rank",
                "output_info",
            ]
        }

    def analysis_(self, code_: str, prob_id: str, stu: str):            
        res_mbfl = ['//'] * 5
        res_sbfl = ['//'] * 4
        # 计算mbfl的结果     
        try:
            res_mbfl = analysis_res_format(
                list(self.get_res(code_=code_, prob_id=prob_id, stu=prob_id)),
                'mbfl'
            )  # list[str]
        except Exception:
            # 算法运行错误
            pass
        # 计算sbfl的结果
        try:
            alg_sbfl.exce_res = self.algorithm.exce_res
            res_sbfl = analysis_res_format(
                list(alg_sbfl.cal(code_=code_, test_case=self.test_cases[prob_id], stu=prob_id)),
                'sbfl'
            )  # list[str]
        except Exception:
            # 算法运行错误
            pass
  
        return res_mbfl, res_sbfl

    def analysis(self, code_: str, prob_id: str, stu: str):
        """
        params:
        :param code_: str, student code
        :param prob_id: str, problem id
        :param stu: str, file_name 
        return:
        0: cut, 1: pass, -1: fail, 2: compile error
        """        
        if prob_id not in self.test_cases:
            logger_.info(f"{stu}: cut prob, continue")
            return 0

        # 跑一遍sbfl即可
        try:
            self.get_res(code_=code_, prob_id=prob_id, stu=stu)
        except sbfl.base.NoFailingTestError as nfte:
            # 完全正确
            logger_.info(f"{stu}-gold_true: NoFailingTestError")                
            return 1
        except FaultLocalizationError as fle:
            # 定位失败
            logger_.info(f"{stu}-gold_false: {fle}")   
            return -1
        except Exception as e:
            # 编译错误
            logger_.info(f"{stu}-sbfl_exception: {e}")
            return 2
        else:
            logger_.info(f"{stu}: gold_false")
            return -1

    def get_res(self, code_: str, prob_id: str, stu: str):
        """
        - code_: str, can be path or pure code
        - prob_id: str
        - stu: str, 学生代码唯一标识
        """
        # problem not included
        if prob_id not in self.test_cases.keys():
            raise TestCasesNotIncludedError

        return self.algorithm.cal(code_=code_, test_case=self.test_cases[prob_id], stu=stu)


    def get_algorithm(self):
        return self.algorithm

    def set_algorithm(self, algorithm: FL_alg):
        self.algorithm = algorithm


class CodeAnalysis:
    """
        analysis code is correct or not.
    """
    def __init__(self, ):
        log_file_name = "tmp/logs/log_analysis_dataset"
        test_cases_folder = "static/data/testcase"

        session_manager = SessionManager()
        logger = Mylogger(session_manager, log_file_name)
        test_cases = TestCasesLoader(test_cases_folder).get_test_cases()
        alg_sbfl = SBFL(cov=Coverage(), my_stdout=CustomStdout(sys.__stdout__), text='sbfl')

        self.FL_app = FaultLoalization(
            test_cases=test_cases,
            logger=logger,
            algorithm=alg_sbfl,
        )

    def isCorrect(self, code_: str, prob_id: str, stu: str):
        """
        ### params:
        :param code_: str, student code
        :param prob_id: str, problem id
        :param stu: stu info str

        ### return:
        0: cut, 1: pass, -1: fail, 2: compile error
        """
        return self.FL_app.analysis(code_=code_, prob_id=prob_id, stu=stu)


if __name__ == "__main__":
    # code analysis
#     code_ = """a=int(input())
# b=int(input())
# if a > b:
#     print(a)
# else:
#     print(a)"""
#     testcase = (["7\n8", "57\n50", "57\n60"], ["8", "57", "60"])

    # code_ = 'a=list(map(str,input().split()))\nb,c=map(int,input().split())\nd=a.copy()\nd[b]=a[c]\nd[c]=a[b]\nprint(d)\n'

#     code_ = \
#     """
# lst=eval(input())
# a=[]
# for x in lst:
#     for n in range[2:int(x)]:
#         if x%n==0:
#             n.append(a)
# print(a)

#     """

    # analysing
    log_file_name = "tmp/logs/log_analysis_dataset"
    test_cases_folder = "static/data/testcase"
    prob2id_folder = "static/prob2id_map"
    src_code_folder = "analysis/ch*_3004"

    session_manager = SessionManager()
    logger = Mylogger(session_manager, log_file_name)
    test_cases = TestCasesLoader(test_cases_folder).get_test_cases()
    # alg_mbfl = MBFL(cov=Coverage(), my_stdout=CustomStdout(sys.__stdout__), text='mbfl')
    alg_sbfl = SBFL(cov=Coverage(), my_stdout=CustomStdout(sys.__stdout__), text='sbfl')

    FL_app = FaultLoalization(
        test_cases=test_cases,
        logger=logger,
        algorithm=alg_sbfl,
    )

    import shutil
    files = os.listdir(src_code_folder)
    for file in tqdm(files, total=len(files)):
        src_path = os.path.join(src_code_folder, file)
        code_ = open(src_path, "r").read()
        prob_id = file.split("-")[1]
        res = FL_app.analysis(
            code_=code_,
            prob_id="3004",
            stu=file
        )
        # 完全正确
        if res == 1:
            shutil.copy(src_path, os.path.join("ast_research/ch_3004/True", file))
        # 逻辑错误
        if res == -1:
            shutil.copy(src_path, os.path.join("ast_research/ch_3004/False", file))

            

    # print(FL_app.analysis(
    #     code_=code_,
    #     prob_id="3004",
    #     stu="test"
    # ))

    # FL_app.analysis(
    #     dataset_path="dataset/val/val_",
    #     report_path="dataset/val/val_c4_true.xlsx",
    # )

    # FL_app.analysis(
    #     dataset_path="static/test_code",
    #     report_path="analysis/mbfl/analysis_c4.xlsx",
    # )

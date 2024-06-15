# 用于从data中已分好类的代码中每个题目随机抽取出50个代码（按学生），用于标注
import os
import random
import sys
sys.path.append(os.getcwd())
import shutil
from ast_research.utils import *

def main(prob_id):
    # src = f"ast_research/data/ch6/{prob_id}/False"
    # 3004不在ch6中
    src = "ast_research/data/ch_3004/False"
    target = f"ast_research/forAnnotation/{prob_id}"
    folder_check(target)
    res = {}
    count = 0

    # 获学生和代码
    for file in os.listdir(src):
        stu = file.split("-")[0]
        if stu not in res:
            res[stu] = []
        res[stu].append(file)

    # 每个人随机取一个
    for stu_files in res.values():
        if len(stu_files) > 0:
            stu_file = stu_files[random.choice(range(0, len(stu_files)))]
            stu_files.remove(stu_file)
            if count < 50:
                code_ = file_reader(os.path.join(src, stu_file))
                if code_.strip() == "":
                    print(f"{stu_file} is empty")
                    continue
                shutil.copy(
                    os.path.join(src, stu_file),
                    os.path.join(target, stu_file),
                )
            count += 1

    # 提交人数不足50，则从已提交的人的多次提交中填充
    if count < 50:
        for i in range(1, 5):
            for stu_files in res.values():
                if len(stu_files) >= i:
                    stu_file = stu_files[random.choice(range(0, len(stu_files)))]
                    stu_files.remove(stu_file)
                    code_ = file_reader(os.path.join(src, stu_file))
                    if code_.strip() == "":
                        print(f"{stu_file} is empty")
                        continue
                    shutil.copy(
                        os.path.join(src, stu_file),
                        os.path.join(target, stu_file),
                    )
                    count += 1
                    if count == 50:
                        print("done")
                        exit(0)

    # 仍不足则返回报错
    if count < 50:
        print("done with no enough files")
        
    print("done with 50 files")


if __name__ == "__main__":
    # prob_ids = ['3416', '2910', '3108', '2911', '2900']
    # for prob_id in prob_ids:
    #     print('-' * 6 + ' ' + prob_id + ' ' + '-' * 6)
    #     main(prob_id)

    main(3004)


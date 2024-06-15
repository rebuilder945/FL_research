# 用于生成dataset/ch4_labeled
import os 
import sys
os.chdir('/home/wdy/code_LLM/FL_research/')
import shutil
import openpyxl
from openpyxl.styles import Alignment
from tqdm import tqdm

# path config
ori_data_path = r'dataset/ch4'
tar_path = r'dataset/ch4_labeled'

def folder_check(path):
    if not os.path.exists(path):
        os.mkdir(path)

# check if it is one-line diff
def compare_code(code1: str, code2: str):
    lines1 = code1.split('\n')
    lines2 = code2.split('\n')    

    if len(lines1) != len(lines2):
        return False    
    
    # 比较两个列表形式的代码,找出不同的行
    diff_lines = [i for i in range(len(lines1)) if lines1[i] != lines2[i]]    
    # 如果只有一个行不同,则输出该行号

    if len(diff_lines) == 1:
        return diff_lines[0] + 1
    # 如果有多行不同,则输出false
    elif len(diff_lines) > 1:
        return False
    # 如果两个代码完全相同,则输出0
    else:
        return False

wb = openpyxl.Workbook()
ws = wb.active
ws.append(['filename', 'code_f', 'code_t', 'diff_line'])

folder_check(tar_path)

count = 0
ori_data = os.listdir(ori_data_path)
for prob_id_ in tqdm(ori_data, total=len(ori_data)):
    prob_path = os.path.join(ori_data_path, prob_id_)
    for name in os.listdir(prob_path):
        name_path = os.path.join(prob_path, name)
        f_f = open(os.path.join(name_path, "false.py"), "r").read()
        t_f = open(os.path.join(name_path, 'true.py'), 'r').read()
        diff_line = compare_code(f_f, t_f)
        if diff_line:
            count += 1
            ws.append([
                name + '-' + prob_id_,
                f_f,
                t_f,
                diff_line
            ])
            folder_check(os.path.join(tar_path, prob_id_))
            tar_name_path = os.path.join(tar_path, prob_id_, name)
            folder_check(tar_name_path)

            shutil.copyfile(
                os.path.join(name_path, 'false.py'),
                os.path.join(tar_name_path, 'false.py')
            )
            shutil.copyfile(
                os.path.join(name_path, 'true.py'),
                os.path.join(tar_name_path, 'true.py')
            )
            with open(os.path.join(tar_name_path, f"{diff_line}.txt"), "w") as f:
                pass
        else:
            continue

for row in ws.iter_rows():
    for cell in row:
        cell.alignment = Alignment(wrapText=True)

wb.save(f"dataset/ch4_labeled_dataset.xlsx")
print(count)

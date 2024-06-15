# 用于从python_code_5.23中初筛特定章节和特定题目的代码，可直接分类为True和False
import os
import sys
from tqdm import tqdm
sys.path.append("/home/wdy/code_LLM/FL_research")
import shutil
from ast_research.utils import *
from implement.techs import CodeAnalysis

needed_probs = ['3416', '2910', '3108', '2911', '2900', '3004']
count = {}
correct_map = {1: 'True', -1: 'False'}
codeAnalysis = CodeAnalysis()
log_file = open('analysis/log', 'w')

def copy_files_with_name(src_folder, dst_folder):    
    files = os.listdir(src_folder)
    for file in tqdm(files, total=len(files)):
        src_file_path = os.path.join(src_folder, file)
        prob_id = file.split('-')[1]
        if prob_id in needed_probs and 'pyc' not in file:
            log_file.write(f'{file}\n')
            # 判断代码是否正确
            try:
                code_ = file_reader(src_file_path)
            except Exception:
                print(f'{file} 读取失败')
                continue
            if 'exit(' in code_:
                print(f'{file} 存在exit()')
                continue

            iscorrect = codeAnalysis.isCorrect(
                code_=code_,
                prob_id=prob_id,
                stu=file
            )
            
            # count
            if prob_id not in count:
                count[prob_id] = {}
            if iscorrect not in count[prob_id]:
                count[prob_id][iscorrect] = 0
            count[prob_id][iscorrect] += 1

            # 编译错误或其他问题直接跳过
            if iscorrect != 1 and iscorrect != -1:
                continue
            iscorrect = correct_map[iscorrect]

            # 将代码复制到目标分类的文件夹下
            dst_file_path = os.path.join(
                os.path.join(dst_folder, prob_id, iscorrect, file)
            )
            folder_check(os.path.dirname(dst_file_path))
            shutil.copy(src_file_path, dst_file_path)

            

    import json
    with open('analysis/count.json', 'w') as count_f:
        json.dump(count, count_f)
    print('done!')

if __name__ == '__main__':
    src_folder = r'ast_research/python_code_5.23/lastterm_page6/success_code'  # 源文件夹路径
    dst_folder = 'ast_research/data/ch6'  # 目标文件夹路径
    try:
        copy_files_with_name(src_folder, dst_folder)
    except:
        log_file.close()

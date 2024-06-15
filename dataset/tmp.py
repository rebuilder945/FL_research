import os
import shutil
ori_p = r'dataset/ch4/3004'
tg_p = r'ast_research/test_code_1'
for index, name in enumerate(os.listdir(ori_p)):
    ori_path = os.path.join(ori_p, name, 'false.py')
    tg_path = os.path.join(tg_p, f'{index}.py')
    shutil.copy(ori_path, tg_path)
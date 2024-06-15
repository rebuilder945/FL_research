import os 
import shutil
from tqdm import tqdm


def get_last2list(ori_data_path: str):
    # rules
    prob_set = {}
    for f in os.listdir(ori_data_path):
        prob_id = '-'.join(f.split('-')[:2])
        time_stamp = '-'.join(f.split('-')[-2: ])
        if prob_id not in prob_set:
            prob_set[prob_id] = []
        prob_set[prob_id].append(time_stamp)
    # sort
    for _, time_stamps in prob_set.items():
        time_stamps.sort()
    # copy
    last2list = [] # [(prob_id_, last2, last1)...]
    for prob_id, time_stamps in tqdm(prob_set.items()):
        if len(time_stamps) >= 2:
            f_name_0 = prob_id + '-2023-' + time_stamps[-2]
            f_name_1 = prob_id + '-2023-' + time_stamps[-1]
            last2list.append((prob_id, f_name_0, f_name_1))
    return last2list

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

def folder_check(path):
    if not os.path.exists(path):
        os.mkdir(path)

# # path config
# ori_data_path = r'dataset/ch4_gold'
# # ori_data_path = r'dataset/ch4_gold'
# tar_data_path = r'dataset/ch4'
# val_path = r'dataset/val'

# if not os.path.exists(tar_data_path):
#     os.mkdir(tar_data_path)



# # sort
# for _, time_stamps in prob_set.items():
#     time_stamps.sort()

# # copy
# for prob_id, time_stamps in tqdm(prob_set.items()):
#     if len(time_stamps) < 2:
#         print(prob_id, time_stamps)
#         continue

#     name, prob_id_ = prob_id.split('-')
#     prob_path = os.path.join(tar_data_path, prob_id_)
#     name_path = os.path.join(prob_path, name)

#     # mkdir if needed
#     if not os.path.exists(prob_path):
#         os.mkdir(prob_path)
#     if not os.path.exists(name_path):
#         os.mkdir(name_path)
    
#     # which files selected to copy: last time submit and second last time submit
#     f_name_0 = prob_id + '-2023-' + time_stamps[-2] # second last        
#     src_0 = os.path.join(ori_data_path, f_name_0) # 倒二次
#     dst_0 = os.path.join(name_path, 'false.py')
#     shutil.copyfile(src_0, dst_0)
#     # shutil.copyfile(src_0, os.path.join(val_path, 'val_', f_name_0)) # copy to val

#     f_name_1 = prob_id + '-2023-' + time_stamps[-1] # last 
#     src_1 = os.path.join(ori_data_path, f_name_1) # 最后一次
#     dst_1 = os.path.join(name_path, 'true.py')
#     shutil.copyfile(src_1, dst_1)
#     # shutil.copyfile(src_1, os.path.join(val_path, 'val_', f_name_1)) # copy to val

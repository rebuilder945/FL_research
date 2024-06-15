import os
os.chdir(r'/home/wdy/code_LLM/FL_research')
import shutil
src_path = r'dataset/val/gold_true'
search_path = r'dataset/val/gold_false'

# 遍历search_path
t = {}
for f in os.listdir(search_path):
    prob_id = '-'.join(f.split('-')[:2])
    if prob_id not in t:
        t[prob_id] = []
    t[prob_id].append(f)

# 从src_path中匹配search_path中
a = 0
for f in os.listdir(src_path):
    prob_id = '-'.join(f.split('-')[:2])
    # time_stamp = '-'.join(f.split('-')[-2:])
    # shutil.copyfile(os.path.join(search_path, t[prob_id][0]), os.path.join(r'dataset/ch4_gold_false',  t[prob_id][0]))
    try:
        shutil.copyfile(os.path.join(search_path, t[prob_id][0]), os.path.join(r'dataset/ch4_gold_false',  t[prob_id][0]))
    except:
        continue
    shutil.copyfile(os.path.join(src_path, f), os.path.join(r'dataset/ch4_gold_true', f))
    a += 1
print(a)



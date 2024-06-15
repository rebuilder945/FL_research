s = input()
max_str = "" # 最长数字子串
cur_str = "" # 当前数字子串
for i in s:
    if i.isdigit(): # 如果当前字符是数字
        cur_str += i # 更新当前数字子串
    else: # 如果当前字符不是数字
        if len(cur_str) >= len(max_str): # 如果当前数字子串比最长数字子串更长或一样长
            max_str = cur_str # 更新最长数字子串
        cur_str = "" # 重置当前数字子串
if len(cur_str) >= len(max_str): # 处理字符串末尾的情况
    max_str = cur_str
if len(max_str) == 0: 
    print("No digits")
else:
    print(max_str)
        

s = input()  # 读入字符串
max_str = ""  # 最长数字子串
tmp_str = ""  # 当前数字子串
for c in s:
    if c.isdigit():
        tmp_str += c
    else:
        if tmp_str and len(tmp_str) >= len(max_str):  # 如果tmp_str不为空且长度大于等于max_str
            max_str = tmp_str  # 更新最长数字子串
        tmp_str = ""  # 清空当前数字子串
if tmp_str and len(tmp_str) >= len(max_str):  # 判断最后一个数字子串是否为最长数字子串
    max_str = tmp_str
if max_str:
    print(max_str)
else:
    print("No digits")


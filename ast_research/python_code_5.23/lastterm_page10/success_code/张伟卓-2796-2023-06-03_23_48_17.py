s = input()  # 读入字符串
n = len(s)   # 字符串长度
num_list = []  # 数字子串列表
num_str = ""   # 数字子串
for i in range(n):
    if s[i].isdigit():  # 如果当前字符是数字
        num_str += s[i]  # 把数字字符添加到当前数字子串
    elif num_str != "":  # 如果当前字符不是数字且数字子串不为空
        num_list.append(num_str)  # 保存当前数字子串到数字子串列表
        num_str = ""  # 重置当前数字子串
if num_str != "":
    num_list.append(num_str)

if not num_list:  # 如果数字子串列表为空
    print("No digits")
else:
    max_len = max(len(num) for num in num_list)  # 最长数字子串的长度
    for num in num_list[::-1]:  # 反向遍历数字子串列表
        if len(num) == max_len:  # 找到第一个最长的数字子串并输出
            print(num)
            break

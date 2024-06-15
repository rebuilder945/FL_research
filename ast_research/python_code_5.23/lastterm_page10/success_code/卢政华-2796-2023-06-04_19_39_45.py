string = input()  # 读入一个字符串

digit_substrings = [s for s in string.split() if s.isdigit()]  # 提取所有的数字子串
if not digit_substrings:  # 如果没有数字子串
    print('No digits')
else:
    print(max(digit_substrings, key=len))  # 输出最长的数字子串

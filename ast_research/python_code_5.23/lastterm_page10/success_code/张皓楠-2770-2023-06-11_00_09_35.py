s = input()
if not any(c.isdigit() for c in s):
    print("No digits")  # 字符串中没有数字字符，输出"No digits"
else:
    digits = []  # 存储数字子串
    for i in range(len(s)):
        if s[i].isdigit():  # 当前字符是数字，则加入数字子串
            if i > 0 and s[i-1].isdigit():
                digits[-1] += s[i]  # 如果上一个字符也是数字，则与上一个数字合并
            else:
                digits.append(s[i])  # 否则将当前数字加入数字子串
    max_len = 0
    b=[]
    for digit in digits:
        if len(digit) >= max_len:
            max_len = len(digit)
            b.append(digit)
    print(b[-1])  # 输出最长数字子串









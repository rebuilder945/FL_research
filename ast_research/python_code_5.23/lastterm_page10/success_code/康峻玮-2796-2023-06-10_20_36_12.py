s = input()          # 读入字符串
digit_str = ''       # 记录当前的数字子串
max_digit_str = ''   # 记录最长的数字子串
for c in s:
    if c.isdigit():                  # 如果字符是数字
        digit_str += c               # 将其添加到当前数字子串末尾
    else:                            # 否则
        if digit_str:                # 如果当前数字子串不为空
            if len(digit_str) >= len(max_digit_str):  # 如果当前数字子串比之前的最长数字子串更长
                max_digit_str = digit_str            # 更新最长数字子串
            digit_str = ''             # 清空当前数字子串
if digit_str:            # 处理最后一段数字子串
    if len(digit_str) >= len(max_digit_str):
        max_digit_str = digit_str
if max_digit_str:
    print(max_digit_str)
else:
    print('No digits')

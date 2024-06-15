string = input()  # 输入字符串

# 初始化各类字符数量为0
letter_count = 0
space_count = 0
digit_count = 0
other_count = 0

# 遍历字符串中的每个字符，判断其属于哪一类
for char in string:
    if char.isalpha():  # 判断是否为英文字符
        letter_count += 1
    elif char.isspace():  # 判断是否为空格字符
        space_count += 1
    elif char.isdigit():  # 判断是否为数字字符
        digit_count += 1
    else:  # 其他字符均视为其他类型的字符
        other_count += 1

# 输出各类字符数量
print(letter_count, space_count, digit_count, other_count)

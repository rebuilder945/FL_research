s = input("请输入一个字符串：")
char_count, space_count, num_count, other_count = 0, 0, 0, 0
for i in s:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        #使用了错误的操作符 +，这里不需要使用 + 操作符。
        char_count += 1
    elif i == " ":
        space_count += 1
    elif i.isdigit():  # 使用isdigit()方法检查是否为数字
        num_count += 1
    else:
        other_count += 1
print(char_count, space_count, num_count, other_count)

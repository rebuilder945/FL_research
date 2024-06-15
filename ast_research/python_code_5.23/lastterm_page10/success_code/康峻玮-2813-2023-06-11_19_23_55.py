string = input()  # 输入字符串
sub_string = input()  # 输入需要删除的子串

new_string = string.replace(sub_string, "")  # 删除子串

print(new_string)

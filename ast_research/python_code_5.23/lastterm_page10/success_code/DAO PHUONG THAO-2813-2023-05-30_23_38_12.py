def remove_substring(string, substring):
    # 使用 replace 函数将子串替换为空字符串
    result = string.replace(substring, '')

    return result

# 读取输入的字符串和子串
string = input()
substring = input()

# 删除字符串中的子串并输出结果
result = remove_substring(string, substring)
print(result)




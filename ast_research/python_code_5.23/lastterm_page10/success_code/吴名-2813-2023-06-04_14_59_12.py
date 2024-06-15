def remove_substring(string, substring):
    result = string.replace(substring, "")
    return result

# 从标准输入获取字符串和子串
string = input()
substring = input()

# 删除子串并输出结果
result = remove_substring(string, substring)
print(result)


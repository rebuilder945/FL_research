def is_anagram(str1, str2):
    # 判断两个字符串是否为变位词
    if len(str1) != len(str2):
        return False

    # 将字符串转换为字符列表，并排序
    chars1 = sorted(list(str1))
    chars2 = sorted(list(str2))

    # 比较排序后的字符列表是否相同
    return chars1 == chars2

# 读取输入的两个字符串
str1 = input()
str2 = input()

# 判断是否为变位词并输出结果
result = is_anagram(str1, str2)
print(result)




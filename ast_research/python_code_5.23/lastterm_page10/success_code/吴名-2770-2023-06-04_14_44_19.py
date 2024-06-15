def is_anagram(str1, str2):
    # 将两个字符串转换为小写，并排序
    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())
    
    # 比较排序后的字符串是否相等
    if str1 == str2:
        return True
    else:
        return False

# 从标准输入获取两个字符串
str1 = input()
str2 = input()

# 判断是否为变位词并输出结果
result = is_anagram(str1, str2)
print(result)


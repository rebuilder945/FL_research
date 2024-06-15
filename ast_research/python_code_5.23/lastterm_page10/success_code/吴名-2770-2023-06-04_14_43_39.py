def is_anagram(str1, str2):
    # 判断两个字符串是否为变位词
    # 去除空格并将字符串转换为小写，便于比较
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # 长度不同的字符串不可能是变位词
    if len(str1) != len(str2):
        return False
    
    # 使用字典记录每个字符出现的次数
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # 遍历第二个字符串，减少计数器的值
    # 如果计数器小于等于0，说明字符不匹配，不是变位词
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] <= 0:
                del char_count[char]
        else:
            return False
    
    # 如果字典为空，则说明所有字符都匹配成功，是变位词
    return len(char_count) == 0

# 从标准输入获取两个字符串
str1 = input()
str2 = input()

# 判断是否为变位词并输出结果
result = is_anagram(str1, str2)
print(result)


def count_letters(str_list):
    # 初始化一个字典，用于存放字母出现次数
    letter_count = {}
    for i in range(26):
        letter_count[chr(ord('a') + i)] = 0  # 字母从a到z，按照ascii码递增

    # 遍历列表中的每个字符串，统计每个字母出现的次数
    for s in str_list:
        for c in s:
            if c.isalpha() and c.islower():
                letter_count[c] += 1

    # 按照a-z的顺序输出结果
    result = ''
    for i in range(26):
        letter = chr(ord('a') + i)
        result += f"{letter},{letter_count[letter]}\n"
    return result

# 测试样例
str_list = eval(input("请输入一个仅包含字符串对象的列表，字符串对象中仅出现小写英文字母，如：['abc', 'def', 'ghi']："))
print(count_letters(str_list))


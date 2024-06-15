from collections import defaultdict

def count_letters(str_list):
    letter_count = defaultdict(int)
    for string in str_list:
        for char in string:
            letter_count[char] += 1

    for char in sorted(letter_count.keys()):
        print(char + "," + str(letter_count[char]))

# 读取字符串列表
str_list = eval(input())

# 统计字母出现次数并输出结果
count_letters(str_list)


from collections import Counter

def count_letters(strings_list):
    # 创建一个字典，用于存储每个字母的出现次数
    letter_count = {}

    # 遍历列表中的每个字符串
    for string in strings_list:
        # 将字符串转换为字符列表
        letters = list(string)

        # 遍历字符列表，更新字母出现次数
        for letter in letters:
            if letter.islower():
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1

    # 按字母顺序输出每个字母及其出现次数
    for letter, count in sorted(letter_count.items()):
        print(f"{letter},{count}")

# 示例输入
input_list = input()

# 调用函数，输出结果
count_letters(input_list)


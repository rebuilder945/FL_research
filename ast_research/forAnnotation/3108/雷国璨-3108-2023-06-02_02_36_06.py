from collections import Counter

def count_letters(str_list):
    # 将所有字符串连接起来，计算每个字母出现的次数
    all_letters = ''.join(str_list)
    letter_count = Counter(all_letters)
    # 按a-z的顺序输出
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        count = letter_count.get(letter, 0)
        print(f'{letter},{count}')

# 测试样例
str_list = ["aaab", "cccdz"]
count_letters(str_list)

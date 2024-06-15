def count_letters(str_list):
    # 使用字典记录每个字母出现的次数
    letter_count = {}
    for s in str_list:
        for c in s:
            if c in letter_count:
                letter_count[c] += 1
            else:
                letter_count[c] = 1
    # 按a-z的顺序输出
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        count = letter_count.get(letter, 0)
        print(f'{letter},{count}')

# 测试样例
str_list = ["aaab", "cccdz"]
count_letters(str_list)

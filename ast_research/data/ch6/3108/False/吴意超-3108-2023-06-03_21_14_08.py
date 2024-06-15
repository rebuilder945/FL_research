from collections import Counter
import ast
def count_letters(string_list):
    # 将字符串列表中的字符连接成一个大字符串，然后转为Counter对象进行统计
    counter = Counter(''.join(string_list))

    # 按a-z顺序输出结果
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        print(f"{letter},{counter[letter]}")

string_list = ast.literal_eval(input())

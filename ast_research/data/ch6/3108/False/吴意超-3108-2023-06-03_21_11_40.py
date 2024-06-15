from collections import Counter
import ast

def count_letters():
    # 读取字符串列表输入（字符串格式的列表）
    string_list = ast.literal_eval(input())

    # 将字符串列表中的字符连接成一个大字符串，然后转为Counter对象进行统计
    counter = Counter(''.join(string_list))

    # 按a-z顺序输出结果
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        print(f"{letter},{counter[letter]}")

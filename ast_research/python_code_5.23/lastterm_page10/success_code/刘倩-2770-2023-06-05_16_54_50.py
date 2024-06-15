string1 = input()  # 输入第一个字符串
string2 = input()  # 输入第二个字符串

if sorted(string1) == sorted(string2):  # 对两个字符串进行排序，并比较排序后的结果
    print(True)  # 排序后相等，说明是变位词
else:
    print(False)  # 排序后不相等，说明不是变位词


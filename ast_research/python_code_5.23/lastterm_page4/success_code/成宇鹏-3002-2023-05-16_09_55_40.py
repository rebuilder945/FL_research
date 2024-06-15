# 输入一个整数列表，计算所有元素的平均值，如果结果中小数为0，请只输出整数部分，如果结果中的小数部分不为0，则输出结果保留两位小数。


lst = eval(input())
a = sum(lst)
b = len(lst)
c = a/b
if a%b == 0:
    print(int(c))
else:
    print("%.2f"%c)

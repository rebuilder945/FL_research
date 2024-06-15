#【问题描述】
#读入一个列表lst和正整数n和m，然后删除n~m之间的元素，不包括m位置的元素，
#其中n小于或者等于m。如果输入的n和m不在列表lst的下标范围内，则输出"error"。
#【输入形式】
#第一行输入列表。包含方括号，列表元素用逗号分隔。
#第二行输入两个整数n和m，中间用一个逗号分割。
#【输出形式】
#直接用print输出列表
lst1 = eval(input())
n,m = eval(input())
if n>m or int(n)>len(lst1) or int(m)>len(lst1):
    print("error")
else:
    del lst1[n:m]
    print(lst1)


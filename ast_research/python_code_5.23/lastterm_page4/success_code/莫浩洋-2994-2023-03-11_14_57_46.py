'''输入一个整数列表和整数n(n可以是负数）和正整数m，从该列表中选择第n个元素，把该元素重复m次，然后放到列表的尾端，最后输出列表。如果输入的n值不在列表下标范围之内，则输出"error"
【输入形式】
输入时，第一行输入列表的元素，用英文逗号分隔。
第二行输入两个数字n和m，用英文逗号分隔。
【输出形式】
直接使用print输出列表
【样例输入1】
1,2,3,4,5
2,3
【样例输出1】
[1, 2, 3, 4, 5, 3, 3, 3]'''
list1 = eval(input())
n,m = eval(input())
if n > len(list1)-1:
    print("error")
else:
    a = list1[n]
    for i in range(m):
        list1.append(a)
    print(list1)

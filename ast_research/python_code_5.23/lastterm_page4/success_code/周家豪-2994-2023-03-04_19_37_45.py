# 输入一个整数列表和整数n(n可以是负数）和正整数m，从该列表中选择第n个元素，把该元素重复m次，
# 然后放到列表的尾端，最后输出列表。如果输入的n值不在列表下标范围之内，则输出"error"

lst1=input().split(",")
n,m=eval(input())
lst1=list(map(int,lst1))
if n<=-len(lst1)-1 or n==0 or n>=len(lst1):
    print("error")
else:
    lst2=[lst1[n] for i in range(0,m)]
    lst1.extend(lst2)
    print(lst1)

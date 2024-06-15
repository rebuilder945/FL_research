# 交换列表中两个元素的值，并输出列表
lst=input(int()).split(" ")
n,m=eval(input())
a=lst[n]
b=lst[m]
lst1=lst
lst[n]=b
lst[m]=a
print(lst1)

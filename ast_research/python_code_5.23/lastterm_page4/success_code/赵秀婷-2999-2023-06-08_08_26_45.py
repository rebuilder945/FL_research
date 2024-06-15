# 交换列表中两个元素的值，并输出列表
lst=input().split(" ")
n,m=eval(input())
lst[n],lst[m]=lst[m],lst[n]
print(lst)

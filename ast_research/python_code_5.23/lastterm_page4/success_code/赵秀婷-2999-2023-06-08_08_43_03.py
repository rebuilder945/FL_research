# 交换列表中两个元素的值，并输出列表
# lst=map(input().split())
# n,m=map(int,input().split())
# a=lst[n]
# b=lst[m]
# lst[n]=b
# lst[m]=a
# print(lst)

list1=input().split()
m,n=input().split()
a=int(m)
b=int(n)
q=list1[a]
list1[a]=list1[b]
list1[b]=q
print(list1)

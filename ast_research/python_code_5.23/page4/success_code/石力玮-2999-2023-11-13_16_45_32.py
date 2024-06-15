a=input()
n,m=int(input())
list=a.split(' ')
list1=list.copy()
list1[n]=list[m]
list1[m]=list[n]
print(list1)


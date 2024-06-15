a=input()
n,m=eval(input())
list=a.split(' ')
list1=list.copy()
list1[n]=list[m]
list1[m]=list[n]
print(list1)


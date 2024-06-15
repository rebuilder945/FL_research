list1=input().split()
list2=input().split()
n=eval(list2[0])
m=eval(list2[1])
list1[n],list1[m]=list1[m],list1[n]
print(list1)


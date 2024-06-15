a=input()
list1=a.split()
n,m=input().split()
n,m=int(n),int(m)
list1[n],list1[m]=list1[m],list1[n]
print(list1)

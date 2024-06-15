
list1=input().split()
n,m=input().split()
n,m = int(n),int(m)
temp =list1[m] 

list1[n],list1[m] = list1[m],list1[n]
print(list1)



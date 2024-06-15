
list1=input().split()
n,m=input().split()
n,m = int(n),int(m)
aa=list1[n]
bb=list1[m]
list1.remove(aa)
list1.remove(bb)
list1.insert(m,aa)
list1.insert(n,bb)
print(list1)



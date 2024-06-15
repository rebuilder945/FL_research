list=input().split(" ")
n,m=input().split()
list2=[list[n],list[m]]
list.pop(n)
list.insert(n,list2[1])
list.pop(m)
list.insert(m,list[1])
print(list)

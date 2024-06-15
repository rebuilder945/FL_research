list=input().split(" ")
list3=input().split( )
n=list3[1]
m=list3[2]
list2=[list[n],list[m]]
list.pop(n)
list.insert(n,list2[1])
list.pop(m)
list.insert(m,list[1])
print(list)

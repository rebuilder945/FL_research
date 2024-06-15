n=int(input())
list=[x for x in range(1,n)]
a=list[0]
list.remove(a)
list.append(a)
print(list)

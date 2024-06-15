n=int(input())
list=[x for x in range(1,n+1)]
a=list[0]
list.remove(a)
list.append(a)
print(list)

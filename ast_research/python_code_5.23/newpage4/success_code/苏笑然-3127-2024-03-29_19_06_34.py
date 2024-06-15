n=int(input())
list=[x for x in range(1,n+1)]
del list[0]
list.append(1)
print(list)

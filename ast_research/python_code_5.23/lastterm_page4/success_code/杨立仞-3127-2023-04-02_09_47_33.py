n=eval(input())
list1=[x+1 for x in range(n)]
del(list1[n-1])
list1[n-2].append(1)
print(list1)

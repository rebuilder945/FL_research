n=eval(input())
a=[x for x in range(1,n+1)]
i=a.pop(0)
a.insert(-1,i)
print(a)

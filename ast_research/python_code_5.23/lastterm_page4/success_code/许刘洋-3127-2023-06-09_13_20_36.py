n=input()
a=[x for x in range(1,n+1)]
x=a.pop(0)
a.insert(-1,x)
print(a)

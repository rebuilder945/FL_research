n=eval(input())
b=[x for x in range(1,n+1,1)]
d=b.copy()
for i in range(1,len(b)):
    c=b.pop(i)
    b.insert(i-1,c)
print(b)




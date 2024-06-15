n=eval(input())
a=[x for x in range(1,n+1)]
b=[]
for i in a:
    if i>1:
        b.append(i)
b.append(1)
print(b)

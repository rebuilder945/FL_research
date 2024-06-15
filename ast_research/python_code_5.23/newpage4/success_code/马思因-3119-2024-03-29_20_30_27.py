n=eval(input())
print(n)
b=[]
for i in range(len(n)-1,0,-1):
    a=n[i]
    if a in b:
        pass
    else:
        b.append(a)
if n[0] in b:
    pass
else:
    b.append(n[0])
b.reverse()
print(b)

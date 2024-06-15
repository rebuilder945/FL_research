a=eval(input())
b=str(a)
b=list(map(str,b))
d=[]
for i in range(len(b)):
    c=int(b[i])
    if c<5:
        c+=5
        d.append(c)
    else:
        c-=5
        d.append(c)
d.reverse()
d=[str(i) for i in d]
e=("".join(d))
print(e)

a=input()
b=list(a)
c=[]
for x in range(len(a)):
    if b[x]in ['1','2','3','4','5','6','7','8','9','0']:
        n=1
        f=[]
        f.append(b[x])
        while b[x+n] in ['1','2','3','4','5','6','7','8','9','0']:
            f.append(b[x+n])
            n+=1
        e=''.join(f)
        c.append(e)
c.reverse()
c.sort(key=len)
print(c[0])

a=input()
b=list(a)
c=[]
for x in range(len(a)):
    if b[x]in ['1','2','3','4','5','6','7','8','9','0']:
        n=1
        f=[]
        f.append(b[x])
        if x==len(a)-1:
            break
        while x+n<=len(a)-1 and b[x+n] in ['1','2','3','4','5','6','7','8','9','0']:
            f.append(b[x+n])
            n+=1
        e=''.join(f)
        c.append(e)
c.sort(key=len)
print(c[-1])

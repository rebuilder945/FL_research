a=eval(input())
b=[i for i in range(1,a+1)]
c=0
n=0
for i in b:
    if c==0:
        n=i
        b[c]=b[c+1]
        c=c+1
    elif c==len(b)-1:
        break
    else:
        b[c]=b[c+1]
        c=c+1
b[c]=n
print(b)

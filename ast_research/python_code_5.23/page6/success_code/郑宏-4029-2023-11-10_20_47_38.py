a,b=input().split()
a=int(a)
a=max(a,1)
b=int(b)
if a>b or a<0 or b<0 or a>9 or b>9:
    print('illegal input')
else:
    c=list(range(a,b))
    d=[str(x)+str(y)+str(z) for x in c for y in c for z in c if x!=y and x!=z and y!=z]
    for i in d:
        s=str(i)
        if s[0]=='0':
            continue
        else:
            print(i,end=' ')



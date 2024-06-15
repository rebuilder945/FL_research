a,b=input().split()
a=int(a)
b=int(b)
if a>b or a<0 or b<0 or a>9 or b>9:
    print('illegal input')
else:
    c=list(range(a,b))
    d=[str(x)+str(y)+str(z) for x in c for y in c for z in c if x!=y and x!=z and y!=z]
    for i in d:
        print(i,end=' ')

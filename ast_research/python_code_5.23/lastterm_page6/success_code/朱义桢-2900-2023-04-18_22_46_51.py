a=eval(input())
if a<=1 or type(a)!=int:
    print("illegal input")
else:
    b=[x for x in range(2,a+1)]
    c=[]
    for i in b:
        for x in range(2,i//2+1):
            if i%x==0:
                pass
                break
        else:
            c.append(i)
    d=[]
    for x in c:
        if str(x)==str(x)[::-1]:
            c.append(x)
        else:
            pass
    for x in d[:]:
        print(x,end=' ')

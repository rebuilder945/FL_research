ls=str(input())
for x in ls:
    print(x,end="")
ls1=list(ls)
ls2=ls1.copy()
print( )


for i in ls2:
    n=ord(i)
    if n>=65 and n<=90:
        b=chr(155-n)
        ls1[ls2.index(i)]=b
        ls2[ls2.index(i)]=0
    elif  n>=97 and n<=122:
        c=chr(219-n)
        ls1[ls2.index(i)]=c
        ls2[ls2.index(i)]=0
    else:
        ls1[ls2.index(i)]=i
        ls2[ls2.index(i)]=0
print("".join(str(x) for x in ls1))


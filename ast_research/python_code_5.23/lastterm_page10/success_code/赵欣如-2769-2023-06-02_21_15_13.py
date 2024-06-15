ls=str(input())
for x in ls:
    print(x,end="")
ls1=list(ls)
print( )


for i in ls1:
    n=ord(i)
    if n>=65 and n<=90:
        b=chr(155-n)
        ls1[ls1.index(i)]=b
    elif  n>=97 and n<=122:
        c=chr(219-n)
        ls1[ls1.index(i)]=c
    else:
        ls1[ls.index(i)]=i
print("".join(str(x) for x in ls1))


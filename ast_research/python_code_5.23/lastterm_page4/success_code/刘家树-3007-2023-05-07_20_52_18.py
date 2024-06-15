a=eval(input())
b,c=eval(input())
changdu=int(len(a))
if b>changdu:
    print ("error")
elif c>changdu:
    print ("error")
elif b<=c:
    shu=c-b
    while shu>0:
        del a[int(b)]
        shu-=1
    print (a)
elif b>=c:
    shu=b-c
    while shu>0:
        del a[int(c+1)]
        shu-=1
    print (a)




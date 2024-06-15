list=eval(input())
b,c=eval(input())
long=int(len(list ))
if b>long:
    print ("error")
elif c>long:
    print ("error")
elif b>=c:
    shu=b-c
    while shu>0:
        del list[int(c+1)]
        shu-=1
        print(list)
elif b<=c:
    shu=c-b
    while shu>0:
        del list[int(b)]
        shu-=1
    print (list)


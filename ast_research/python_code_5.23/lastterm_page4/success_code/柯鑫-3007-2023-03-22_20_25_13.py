list=eval(input())
a,b=eval(input())
long=int(len(list ))
if a>long:
    print ("error")
elif b>long:
    print ("error")
elif a>=b:
    shu=a-b
    while shu>0:
        del list[int(b+1)]
        shu-=1
        print(list)
elif a<=b:
    shu=b-a
    while shu>0:
        del list[int(a)]
        shu-=1
    print (list)


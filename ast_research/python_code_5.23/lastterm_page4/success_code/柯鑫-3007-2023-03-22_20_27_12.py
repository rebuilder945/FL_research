list=eval(input())
a,b=eval(input())
long=int(len(list ))
if a>long:
    print ("error")
elif b>long:
    print ("error")
elif a>=b:
    cha=a-b
    while cha>0:
        del list[int(b+1)]
        cha-=1
    print(list)
elif a<=b:
    cha=b-a
    while cha>0:
        del list[int(a)]
        cha-=1
    print (list)


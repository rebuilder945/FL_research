list1=eval(input())
c,d=map(int,input().split(','))

a=max(list1)
b=min(list1)


if a>=c>=d>=b :
    for i in list1:
        if c>i>d :
            list1.remove(i)
            print(list1)
else:
    print("error")
    


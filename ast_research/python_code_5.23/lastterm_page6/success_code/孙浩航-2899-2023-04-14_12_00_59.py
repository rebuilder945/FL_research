a=input().split()
if len(range(int(a[0]),int(a[-1])))<3 or int(a[-1])>11 or int(a[0])<0:
    print("illegal input")
else:
    for x in range(int(a[0]),int(a[-1])):
        for y in range(int(a[0]),int(a[-1])):
            for z in range(int(a[0]),int(a[-1])):
                if not x==y and not x==z and not z==y:
                    n=x*100+y*10+z
                    if n>=100:
                     print(n,end=" ")



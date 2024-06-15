def  allnum(n):
    n = int(input())
    allnum = []
    if n<=0 or n%1 != 0:
        print("illegal input")
    else:
        for i in range(1,n+1,1):
            for j in range(2,i):
                if i%j != 0:
                    a=str(i)
                    b=len(a)
                    for x in range(1,b+1,1):
                        if a[x] == a[-x]:
                            allnum.append(i)
                        else:
                            i = False
    print(str(allnum))



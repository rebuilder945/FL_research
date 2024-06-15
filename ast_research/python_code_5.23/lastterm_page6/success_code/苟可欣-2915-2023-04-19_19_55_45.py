def shui(m):
    lst=[]
    for x in range(10):
        for y in range(10):
            for z in range(10):
                k=x**3+y**3+z**3
                if k==x*100+y*10+z*1:
                    if k<=m and k>=100:
                        lst.append(k)
    if lst==[]:
        print("none")
    else:
        for i in lst:
            print(i)
m=eval(input())
shui(m)

n,m=input().split(" ")
n=int(n)
m=int(m)
sums=[]
sums1=[]
if(m<n) or (m-n)<3 or m<0 or n<0 or n>8:
    print("illegal input")
else:
    for x in range(n,m):
        sums.append(x)
    for x in range(len(sums)):
        for y in range(len(sums)):
            for z in range(len(sums)):
                if x!=y and y!=z and x!=z and sums[x]!=0:                   
                    s1=str(sums[x])+str(sums[y])+str(sums[z])
                    if s1 not in sums1:
                        sums1.append(s1)
                    else:
                        pass
                else:
                    pass
                   
    for y in sums1:
        y=int(y)
        print("%d "%y,end="")
#————————————————
#版权声明：本文为CSDN博主「谭你一个脑瓜崩」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_54226199/article/details/127326303

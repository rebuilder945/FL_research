n,m=input().split()
n = int(n)
m = int(m)
ls = []
ls2 = []
if n<0 or m<0 or type(n)!=type(1) or type(m)!=type(1) or n>m or m-n<3 or n>7:
    print("illegal input")
else:
    for i in range(n,m):
        ls.append(i)
    for x in ls:
        for y in ls:
            for z in ls:
                if x!=y and x!=z and y!=z:
                    num = str(x)+str(y)+str(z)
                    if num not in ls2:
                        ls2.append(num)
for x in ls2:
    print(x,end=" ")                        



n,m=input().split()
n=int(n)
m=int(m)
lis=[]
if m-n<3 or n>m or n<0 or m<0 or m>10:
    print('illegal input')
else:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=0 and x!=y and y!=z and x!=z:
                    num=f"{x}{y}{z}"
                    lis.append(num)
for i in lis:
    print(i,end=" ")


num=input()
lis=[]
for i in num:
    i=int(i)
    a=(i+5)%10
    lis.append(a)
lis.reverse()
for i in lis:
    print(i,end="")


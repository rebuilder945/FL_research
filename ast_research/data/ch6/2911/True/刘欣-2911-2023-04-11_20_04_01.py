shuzi=input()
lis=[]
for i in range(len(shuzi)):
    lis.append(int(shuzi[i]))
for x in range(len(lis)):
    lis[x]+=5
    lis[x]=lis[x]%10
lis.reverse()
for n in lis:
    print("%s"%n,end="")

num=input()
ls=list(num)
for x in range(len(ls)):
    ls[x]=int(ls[x])
    ls[x]=(ls[x]+5)%10
ls[0],ls[-1]=ls[-1],ls[0]
ls[1],ls[-2]=ls[-2],ls[1]
print(''.join(map(str, ls)))

    


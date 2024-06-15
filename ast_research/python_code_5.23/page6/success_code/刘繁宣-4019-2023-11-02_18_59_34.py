n=eval(input())
ls=[]
for i in range(len(str(n))):
    ls.append((int(str(n)[i])+5)%10)
ls[0],ls[-1]=ls[-1],ls[0]
ls[1],ls[-2]=ls[-2],ls[1]
m=str(ls[0])
for i in range(len(ls)-1):
    m += str(ls[i+1])
print(m)


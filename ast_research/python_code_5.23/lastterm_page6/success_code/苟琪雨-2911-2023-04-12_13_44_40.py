n=input()
lis=[]
for i in n:
    p=int(i)
    m=(p+5)%10
    a=str(m)
    lis.append(a)
lis1=lis.copy()
lis[0]=lis1[-1]
lis[-1]=lis1[0]
lis[1]=lis1[-2]
lis[-2]=lis1[1]
y=""
for x in range(len(lis)):
    y=y+lis[x]
result=y
print(result)

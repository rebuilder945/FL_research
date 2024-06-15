m1=input()
a=[int(x) for x in m1]
n1=[]
for x in a:
    b=int(x)+5
    c=b%10
    n1.append(c)
n1[0],n1[-1]=n1[-1],n1[0]
n1[1],n1[-2]=n1[-2],n1[1]
c=""
for i in n1:
    c=c+str(i)
print(int(c))

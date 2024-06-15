m1=input()
a=[int(x) for x in m1]
n1=[]
for x in a:
    b=int(x)+5
    c=b%10
    n1.append(c)
    n2=0
    n3=-1
for y in range(len(n1)//2):
    n1[n2],n1[n3]=n1[n3],n1[n2]
    n2=n2+1
    n3=n3-1
c=""
for i in n1:
    c=c+str(i)
print(c)

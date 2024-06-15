a=input()
c=[]
for i in range(len(a)):
    c.append((int(a[i])+5)%10)
for i in range(len(c)//2):
    d=c[i]
    c[i]=c[-i-1]
    c[-i-1]=d
for i in range(len(c)):
    print(c[i],end="")

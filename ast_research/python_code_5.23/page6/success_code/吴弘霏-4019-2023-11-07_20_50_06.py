from calendar import c


a=input()
b=[]
for i in range(len(a)):
    b.append(a[i])
for x in range(len(b)):
    b[x]=(int(b[x])+5)%10
b.reverse()
for y in range(len(b)):
    print(b[y],end="")


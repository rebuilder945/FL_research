a=input()
b=[]
for i in range(len(a)):
    c=(int(a[i])+5)%10
    b.append(c)
b.reverse()
for k in range(len(b)):
    print(b[k],end="")


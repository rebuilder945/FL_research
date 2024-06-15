a=input()
b=[]
c=[]
for i in range(int(a)):
    for j in range(2,i):
        if i%j!=0:
            for p in str(i):
                c.append(p)
            d=c.reverse()
            if d==c:
                b.append(i)
print(b)

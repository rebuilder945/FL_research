a=input().split()
b=a[1:]
b.sort(reverse=True)
print(a[0],end='')
for i in range(len(b)):
    print("%.2f"%int(b[i]),end='')
b=list(map(int,b))
c=sum(b)
print("%.2f"%c)

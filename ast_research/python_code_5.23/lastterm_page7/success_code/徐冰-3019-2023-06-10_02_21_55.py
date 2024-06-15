a=input().split()
for i in range(1,4):
    a[i]=eval(a[i])
b=a[1:4]
b.sort(reverse=True)
avg=sum(a[1:4])/3
a.append(avg)
for i in range(0,5):
    if i==0:
        print(a[i],end=" ")
    else:
        print("%.2f"%a[i],end=" ")



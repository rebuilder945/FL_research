a=eval(input())
for i in range(len(a)):
    a[i]=(a[i]+5)%10
a[0],a[-1]=a[-1],a[0]
a[1],a[-2]=a[-2],a[1]
print(a)

a=str(input())
for i in len(a):
    a[i]=str((int(a[i])+5)%10)
for i in len(a)//2:
    b=a[i]
    a[i]=a[-i-1]
    a[-i-1]=b
print(a)

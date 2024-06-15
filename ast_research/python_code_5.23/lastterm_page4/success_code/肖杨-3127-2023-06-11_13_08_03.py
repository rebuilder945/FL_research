a=eval(input())
a=list(range(1,a+1))
for i in range(len(a)-1):
    a[i]=a[i+1]
a[-1]=1
print(a)


a=eval(input())
b=[]
m=0
for i in range(0,len(a)):
    if a[i]==1 or a[i]==0:
        m=0
    elif a[i]==2:
        m=1
    else:
        for j in range(2,a[i]):
            if a[i]%j!=0:
                m=1
            else:
                m=0
                break
    if m==1:
        b.append(a[i])
print(b)


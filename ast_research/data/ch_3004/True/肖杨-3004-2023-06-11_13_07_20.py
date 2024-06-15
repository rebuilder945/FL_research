def susu(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
a=eval(input())
b=[]
c=[]
for i in range(len(a)):
    if susu(a[i]) is True and a[i]!=0 and a[i]!=1:
        b.append(a[i])
print(b)


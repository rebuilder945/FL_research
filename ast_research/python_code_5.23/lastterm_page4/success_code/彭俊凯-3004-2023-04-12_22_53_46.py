def susu(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
a=eval(input())
b=[]
for i in range(len(a)):
    if susu(a[i]) is True:
        b.append(a[i])
for i in range(len(b)):
    if b[i]==0 or b[i]==1:
        del b[i]
print(b)

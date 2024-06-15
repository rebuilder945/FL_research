def susu(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
a=eval(input())
b=[]
for i in range(len(a)):
    if susu(a[i]) is True or a[i]==1 or a[i]==0:
        b.append(a[i])
print(b)

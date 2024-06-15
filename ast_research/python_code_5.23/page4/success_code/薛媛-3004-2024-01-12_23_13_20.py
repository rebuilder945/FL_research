def sushu(x):
    for i in range(2,x):
        if x%i==0 and x==1:
            return False
    else:
        return True
a=eval(input())
b=[]
for i in range(len(a)):
    if sushu(a[i]):
        b.append(a[i])
print(b)



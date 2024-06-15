def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
a=eval(input())
a1=[]
for i in range(len(a)):
    if type(sushu(a[i]))==True:
        a1.append(a[i])
print(a1)

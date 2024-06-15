def sushu(x):
    if x>=2 and type(x)==int:
        for i in range(2,x//2+1):
            if x%i==0:
                return False
        return True
    else:
        return False
a=eval(input())
b=[]
for i in a:
    if sushu(i)==True:
        b.append(i)
print(b)

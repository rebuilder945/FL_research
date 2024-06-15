def sushu(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5+1)):
        if x%i==0:
            return False
    return True
a=eval(input())
b=[]
for i in a:
    if sushu(i)==True:
        b.append(i)
print(b)
    

def sushu(x):
    if x<2 or type(x)!=int:
        return False
    else:
        for i in range(2,x//2+1):
            if x%i==0:
                return False
        return True
a=eval(input())
b=[]
for i in a:
    if sushu(i):
        b.append(i)
b.sort()
print(b)


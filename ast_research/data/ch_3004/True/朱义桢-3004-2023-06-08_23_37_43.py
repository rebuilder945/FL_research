def sushu(x):
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True
a=eval(input())
b=[]
for x in a:
    if x<=1:
        pass
    elif sushu(x):
         b.append(x)
print(b)

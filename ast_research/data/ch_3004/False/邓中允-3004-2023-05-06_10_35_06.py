def sushu(x):
    if x==2:
        return x
    else:
        for i in range(2,x):
            if x%i!=0:
                return x
a=eval(input())
b=[]
for y in a:
    if y==sushu(y):
        b.append(y)
print(b)


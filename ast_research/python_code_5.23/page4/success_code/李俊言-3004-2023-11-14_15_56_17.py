def sushu(x):
    if x>=2 and type(x)==int:
        for y in range(2,x):
            if x%y==0:
                return False
        return True
    return False
a=eval(input())
b=[]
for x in a:
    if sushu(x):
        b.append(x)
print(b)

            






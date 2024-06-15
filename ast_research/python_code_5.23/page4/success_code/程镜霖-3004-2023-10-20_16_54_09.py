a=eval(input())
b=[]
def sushu(x):
    if x<2:
        return False
    for m in range(2,int(x**0.5)+1):
        if x%m==0:
            return False
    return True
for x in a:
    if sushu(x):
        b.append(x)
print(b)




def sushu(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
n=eval(input())
ls=[]
for a in n:
    if sushu(a):
        ls.append(a)
print(ls)


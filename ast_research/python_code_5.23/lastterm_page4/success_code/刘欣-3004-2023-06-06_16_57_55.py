def sushu(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True
lis=eval(input())
lis2=[]
for i in lis:
    i=int(i)
    if sushu(i):
        lis2.append(i)
print(lis2)

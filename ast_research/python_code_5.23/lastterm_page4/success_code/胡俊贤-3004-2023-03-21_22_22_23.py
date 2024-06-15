ls=eval(input())
a=[]
def sushu(i):
    for t in range(1,i//2+1):
        if i % t==0:
            return False
        return True
for i in ls:
    if sushu(i):
        a.append(i)
print(a)


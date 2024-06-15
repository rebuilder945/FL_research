ls=eval(input())
a=[]
def sushu(i):
    for t in range(2,i):
        if i % t==0:
            return False
            break
        return True
for i in ls:
    if sushu(i):
        a.append(i)
print(a)


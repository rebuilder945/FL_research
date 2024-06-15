ls=eval(input())
a=[]
def sushu(i):
    if i>=2:
        for t in range(2,i):
            if i%t==0:
                return False
        return True
    else:
        return False
for i in ls:
    if sushu(i):
        a.append(i)
print(a)
        

ls=eval(input())
a=[]
if 2 in ls:
    a.append(2)
def sushu(i):
    for t in range(2,i//2+1):
        if i%t==0:
            return False
        else:
            return True
for i in ls:
    if sushu(i):
        a.append(i)
print(a)
        

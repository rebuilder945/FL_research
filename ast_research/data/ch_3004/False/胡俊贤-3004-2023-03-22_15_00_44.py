ls=eval(input())
def sushu(i):
    for t in range(2,i):
        if i%t==0:
            return False
        else:
            return True
a=[]
for i in ls:
    if sushu(i):
        a.append(i)
if 2 in ls:
    a.append(2)
print(a)
        

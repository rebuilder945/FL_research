def sushu(X):
    for i in range(2,X):
        if X%i==0:
            c=0
            break
    else:
        c=1
    return c
a=eval(input())
b=[]
for i in a:
    if i>1:
        b.append(i)
for i in b:
    if sushu(i)==1:
        b.append(i)
print(c)        

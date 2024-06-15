def sushu(a):
    for i in range(2,x//2+1):
        if x%i==0:
            return(0)
        else:
            return(x)
a=eval(input())
b=[]
for x in a:
    if sushu(x)==0:
        pass
    else:
        b.append(x)
print(b)

def sushu(x):
    for i in range(2,x//2+1):
        if x%i==0:
            return(0)
    else:
            return(x)
a=eval(input())
b=[]
for x in a:
    if x<=1:
        pass
    elif sushu(x)==0:
        pass
    elif sushu(x)!=0:
        b.append(x)
print(b)

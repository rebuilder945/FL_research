numbers=eval(input())
sushu=[]
for x in numbers:
    for i in range(2,x,1):
        if x%i==0:
            continue    
        elif x==2:
            sushu.append(2)
        elif x==1:
            continue
        else:
            sushu.append(x)
primenumbers=list(set(sushu))
print(primenumbers)

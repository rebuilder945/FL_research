numbers=eval(input())
sushu=[]
for x in numbers:
    for i in range(2,x,1):
        if x==2:
            sushu.qppend(2)    
        elif x%i==0:
            sushu.append(x)
        elif x==1:
            break
        else:
            sushu.append(x)
primenumbers=list(set(sushu))
print(primenumbers)

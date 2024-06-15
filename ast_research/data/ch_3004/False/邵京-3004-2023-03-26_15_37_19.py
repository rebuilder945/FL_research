numbers=eval(input())
sushu=[]
for x in numbers:
    for i in range(2,x,1):
        if x%i==0:
            continue
        else:
            sushu.append(x)
print(sushu)

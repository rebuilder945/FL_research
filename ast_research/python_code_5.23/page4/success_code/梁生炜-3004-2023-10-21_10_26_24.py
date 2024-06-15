ls=eval(input())
x=[]
for i in ls:
    if i>=2:
        for a in range(2,i):
            if a%i==0:
                break
    else:
        x.append(i)
print(x)

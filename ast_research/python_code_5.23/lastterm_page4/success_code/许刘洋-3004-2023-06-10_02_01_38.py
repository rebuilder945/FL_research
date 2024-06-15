a=eval(input())
x=[]
for i in a:
    if i>=2:
        for j in range(2,i):
            if i%j!=0:
                x.append(i)
print(x)

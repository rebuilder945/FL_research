a=eval(input())
b=[]
for x in a:
    for i in range(2,x):
        if x%i==0:
            break
        else:
            if x not in b:
                b.append(x)
print(b)


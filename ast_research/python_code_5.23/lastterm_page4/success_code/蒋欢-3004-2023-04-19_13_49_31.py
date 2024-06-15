a=eval(input())
b=[]
for x in a:
    for i in range(2,x):
        if x%i==0:
            break
        else:
            continue
    b.append(x)
print(b)

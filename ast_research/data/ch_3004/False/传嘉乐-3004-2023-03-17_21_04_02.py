a=eval(input())
b=[]
for x in a:
    y=2
    for y in range(2,x):
        if x%y==0:
            b.append(x)
print(b)


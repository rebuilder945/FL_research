n1=eval(input())
for x in n1:
    for y in range(2,x):
        if x%y==0:
            n1.remove(x)
print(n1)

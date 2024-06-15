a=eval(input())
for x in a:
    for y in range(2,x):
        if x%y==0:
            a.remove(x)
print(a)


def su(x):
    for i in range(2,x):
        if x%i==0:
            return 0
            break
        else:
            return x
a = eval(input())
b =[]
for c in a:
    if su(c)!=0:
        b.append(c)
print(b)

a = list(eval(input()))
for x in a :
    for i in range(2,x):
        if x % i ==0:
            a.remove(x)
print(a)

a = list(eval(input()))
for x in a :
    if x <2:
        a.remove(x)
    else:
        for i in range(2,x):
            if x % i ==0:
               a.remove(x)
               break
        else:
            pass
print(a)



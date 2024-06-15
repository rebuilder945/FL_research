ls = list(eval(input()))
ls2 = []
k = 0
for x in ls:
    if x == 1 or x ==0:
        ls2.append(x)
    else:
        for i in range(2,x):
            if x%i == 0:       
                ls2.append(x)
ls3 = []
for a in ls:
    if a not in ls2:
        ls3.append(a)
print(ls3)

    



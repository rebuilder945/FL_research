lst = eval(input())
new=[]
for x in lst:
    for j in range(1, x):
        if x % j == 0:
            break
        else:
            if x not in new:
                new.append(x)
print(new)


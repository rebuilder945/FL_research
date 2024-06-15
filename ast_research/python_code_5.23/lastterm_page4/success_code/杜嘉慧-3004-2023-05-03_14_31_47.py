lst = eval(input())
new=[]
for x in lst:
    for j in range(2, x):
        if x % j == 0 and x > 2:
            break
        else:
            if x not in new:
                new.append(x)
print(new)


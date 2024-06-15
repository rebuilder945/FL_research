lst = eval(input())
new=[]
for x in lst:
    for j in range(2, x):
        if x % j == 0:
            break
        else:
            new.append(x)
print(new)


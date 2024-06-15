lst = eval(input())
lst1 = []
for x in lst:
    if x <= 2:
        if x < 2:
            lst.remove(x)
        else:
            lst1.append(x)
    elif x > 2:
        for i in range(2,x):
            if x % i == 0:
                lst1.append(x)
print(lst1)


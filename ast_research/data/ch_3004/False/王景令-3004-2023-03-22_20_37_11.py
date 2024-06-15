from cmath import sqrt


lst = eval(input())
a = []
for i in lst:
    for x in range(3,i):
        if i % x == 0 and i != 2:
            continue
        elif i not in a:
            a.append(i)
print(a)


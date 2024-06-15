from cmath import sqrt


lst = eval(input())
a = []
for i in lst:
    for x in range(2,sqrt(i)):
        if i % x == 0 and i not in a:
            a.append(i)


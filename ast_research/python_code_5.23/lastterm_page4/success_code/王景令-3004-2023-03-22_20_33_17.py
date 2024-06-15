from cmath import sqrt


lst = eval(input())
a = []
for i in lst:
    for x in range(3,i):
        if i % 2 != 0 and i % x == 0 and i not in a:
            a.append(i)
print(a)


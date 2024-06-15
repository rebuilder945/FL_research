from cmath import sqrt


lst = eval(input())
a = []
for i in lst:
    for x in range(2,i):
        if i % x == 0 :
            continue
        elif i not in a:
            a.append(i)
print(a)


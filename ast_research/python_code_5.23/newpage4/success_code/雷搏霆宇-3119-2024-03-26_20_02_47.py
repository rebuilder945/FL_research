a = list(eval(input()))
b = []
for i in a:
    t = a.count(i)
    if t != 1:
        a.remove(i)



print(a)



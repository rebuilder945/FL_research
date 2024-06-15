a = eval(input())
for i in a:
    b = a.count(i)-1
    if b > 0:
        for x in range(b):
            a.remove(i)
print(a)



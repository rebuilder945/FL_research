a = eval(input())
b=a.copy()
for i in a:
    c=a.count((i))
    for j in range(c-1):
        b.remove(i)
print(b)




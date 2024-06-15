a = eval(input())
b = a.copy()
max_=max(a)
min_=min(a)
for x in a:
    if x == max_ or x == min_:
        b.remove(x)
print(b)

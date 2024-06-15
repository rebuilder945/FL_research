ls1 = eval(input())
a = max(ls1)
b = min(ls1)
for x in ls1:
    if x == a or x == b:
        ls1.remove(x)
print(ls1)

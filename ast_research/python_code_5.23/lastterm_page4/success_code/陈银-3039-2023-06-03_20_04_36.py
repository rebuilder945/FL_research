lst = eval(input())
new = []
for x in lst:
    if x not in new:
        new.append(x)
a = max(new)
b= min(new)
new.remove(a)
new.remove(b)
print(new)

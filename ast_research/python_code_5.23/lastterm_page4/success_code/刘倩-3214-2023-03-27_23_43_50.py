a = eval(input())
b = []
c = a.count(0)
d = [0]*c
for x in a:
    if x!=0:
        b.append(x)
print(b + d)

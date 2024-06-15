l = []
n = eval(input())
for x in range (n+1):
    l.append(x)
a = l.pop(l[0])
l.append(a)
print(l)

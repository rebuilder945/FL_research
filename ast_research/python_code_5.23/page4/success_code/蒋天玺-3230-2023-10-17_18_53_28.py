a = eval(input())
b = []
c = len(a)
for i in range(c):
    n = max(a)
    b.append(n)
    a.remove(n)
for x in b:
    print(x,end="")



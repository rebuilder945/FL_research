a = list(input())
b = []
for x in a:
    x = (int(x) + 5) % 10
    b.append(x)
b.reverse()
d = "".join(list(map(str,b)))
print(int(d))

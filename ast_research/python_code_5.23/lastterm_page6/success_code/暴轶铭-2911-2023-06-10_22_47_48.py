a = list(input())
b = []
for x in a:
    x = (int(x) + 5) % 10
    b.append(x)
b.reverse()
for i in range(len(b)):
    print(b[i],end="")

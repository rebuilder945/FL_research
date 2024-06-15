a = eval(input())
b = []
for x in range(len(a)):
    b.append(a.pop(a.index(max(a))))
    print(b[x],end="")

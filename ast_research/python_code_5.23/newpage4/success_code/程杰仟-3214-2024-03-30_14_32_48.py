n = eval(input())
for i in n:
    if int(i) == 0:
        n.remove(i)
        n.append(0)
    print(n)

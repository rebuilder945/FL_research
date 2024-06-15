n=eval(input())
for i in range(len(n)):
    if n[i] == 0:
        del n[i]
        n.append(0)
    elif n[0] == 0:
        del n[0]
        n.append(0)
print(list(n))

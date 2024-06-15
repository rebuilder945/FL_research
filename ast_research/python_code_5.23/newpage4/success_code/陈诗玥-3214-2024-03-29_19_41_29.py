n=eval(input())
for i in range(len(n)):
    if n[i] == 0:
        del n[i]
        n.append(0)
else:True
print(list(n))

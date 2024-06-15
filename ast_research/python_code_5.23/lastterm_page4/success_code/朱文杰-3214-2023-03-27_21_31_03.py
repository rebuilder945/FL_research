n=eval(input())
for i in range(n.count(0)):
    n.remove(0)
    n.append(0)
print(n)

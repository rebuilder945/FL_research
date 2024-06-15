n=eval(input())
a=n.count(0)
for i in range(a):
    n.append(0)
    n.remove(0)
print(n)

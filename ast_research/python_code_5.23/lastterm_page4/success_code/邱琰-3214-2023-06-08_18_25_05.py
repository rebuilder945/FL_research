n=eval(input())
a=n.count(0)
while 0 in n:
    n.remove(0)
for i in range(a):
    n.append(0)
print(n)

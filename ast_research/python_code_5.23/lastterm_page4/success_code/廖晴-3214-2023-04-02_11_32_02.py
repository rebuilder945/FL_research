s=eval(input())
a=s.count(0)
for i in range(s.count(0)):
    s.remove(0)
for i in range(a):
    s.append(0)
print(s)

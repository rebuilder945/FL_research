l = eval(input())
a = l.count(0)
while 0 in l:
    l.remove(0)
for i in range (a):
    l.append(0)
print(l)

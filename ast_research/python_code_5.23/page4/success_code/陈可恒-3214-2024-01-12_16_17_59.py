a = eval(input())
b = a.count(0)
while 0 in a:
    a.remove(0)
while b:
    a.append(0)
    b -= 1
print(a)

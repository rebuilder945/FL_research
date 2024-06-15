a = eval(input())
b = 0
for i in a:
    if i == 0:
        b+=1
for x in range(b):
    a.remove(0)
    a.append(0)


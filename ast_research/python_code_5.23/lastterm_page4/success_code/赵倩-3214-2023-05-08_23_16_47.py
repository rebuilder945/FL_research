a = eval(input())

c = 0
for x in a:
    if x==0:
        a.remove(x)
        c+=1
for y in range(c):
    a.append(0)
print(a)






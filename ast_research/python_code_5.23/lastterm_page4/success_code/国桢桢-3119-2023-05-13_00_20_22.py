l = eval(input())
b = len(l)
for i in range (b):
    a = l[i]
    for x in range(i+1,b):
        while a in l:
            l.remove(a)
            b = b-1
print(l)

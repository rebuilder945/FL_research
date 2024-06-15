a = eval(input())
b = [x for x in range(1,a+1)]
c = []
d = []
for i in b:
    if i != 1:
        c.append(i)
    else:
        d.append(i)
print(c+d)
        


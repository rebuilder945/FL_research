lst = eval(input())
a = []

for i in lst:
    c = []
    if i == 2:
        a.append(i)
    elif i == 1:
        continue
    else:
        for x in range(2,i):
            m = i % x
            c.append(m)
        if 0 not in c:
            a.append(i)
                
            
print(a)


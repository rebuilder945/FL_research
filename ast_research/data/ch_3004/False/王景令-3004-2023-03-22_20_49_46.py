lst = eval(input())
a = []
c = []
for i in lst:
    if i == 2:
        a.append(i)
    else:
        for x in range(2,i):
            m = i % x
            c.append(m)
        if 0 not in c:
            a.append(i)
                
            
print(a)


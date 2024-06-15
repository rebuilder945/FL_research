a=eval(input())
c=[]
for i in a:
    if i==2:
        c.append(2)
    else:
        for b in range(2,i):
            if i%b!=0:
                c.append(i)
c.sort()
print(list(set(c)))

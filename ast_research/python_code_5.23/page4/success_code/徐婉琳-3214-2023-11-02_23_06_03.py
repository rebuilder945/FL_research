c=eval(input())
c1=c.copy()
for x in c1:
    if x==0:
        c.remove(x)
        c.append(x)
print(c)


        


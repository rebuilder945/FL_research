a =list(eval(input()))
b= a.count(0)
c=[]
for i in a:
    if not i in c:
        c.append(i)
for x in range(b):
    c.append(0)
print(c)

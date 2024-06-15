a=input()
b=eval(input())
d=a.split(",")
e=[]
c=[]
for i in d :
    for j in b:
        if d.index(i)==b.index(j):
            c.append(i)
            c.append(j)
            e.append(c)
            c.clear()
print(e)



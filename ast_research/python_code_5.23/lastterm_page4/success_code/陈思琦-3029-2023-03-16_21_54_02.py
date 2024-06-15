a=input()
b=eval(input())
d=a.split()
e=[]
c=[]
for i in d :
    for j in b:
        if d.index(i)==b.index(j):
            c.append(i,j)
            e.append(c)
print(e)



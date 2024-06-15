d=input()
b=eval(input())
a=d.split(",")
x=-1
e=[]
for i in a:
    x+=1
    c=[i]
    c.append(b[x])
    e.append(c)
print(e)


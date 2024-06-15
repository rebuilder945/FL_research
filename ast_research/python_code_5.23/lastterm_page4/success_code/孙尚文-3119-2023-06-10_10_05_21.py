a=eval(input())
b=a[::-1]
c=[]
for i in b:
    if i not in c:
        c.append(i)
d=c[::-1]
print(d)

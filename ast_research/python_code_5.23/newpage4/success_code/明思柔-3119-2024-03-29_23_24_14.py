a=eval(input())
b=[]
c=a[::-1]
for i in c:
    if i not in b:
        b.append(i)
d=b[::-1]
print(d)

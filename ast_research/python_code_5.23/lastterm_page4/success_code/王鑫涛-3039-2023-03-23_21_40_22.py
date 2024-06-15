a = list(eval(input()))
a.sort()
b= a.pop(0)
c = a.pop(-1)
a1=[]
a1.append(b)
a1.append(c)
a2=[]
for x in a:
    if not x in a1:
        a2.append(x)
        continue
print(a2)

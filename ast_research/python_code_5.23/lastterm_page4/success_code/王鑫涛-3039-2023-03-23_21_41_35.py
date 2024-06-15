a = list(eval(input()))
b= max(a)
c = min(a)
a1=[]
a1.append(b)
a1.append(c)
a2=[]
for x in a:
    if not x in a1:
        a2.append(x)
        continue
print(a2)

a,b,c=eval(input())
d=[a]
f=a
for i in range(b-1):
    f+=c
    d.append(f)
print(d)



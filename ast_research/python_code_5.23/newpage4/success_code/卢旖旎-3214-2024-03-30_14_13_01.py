a=eval(input())
b=0
for x in a[0:]:
    if x==0:
        a.remove(x)
        b+=1
        continue
for y in range(b):
    a.append(0)
print(a)

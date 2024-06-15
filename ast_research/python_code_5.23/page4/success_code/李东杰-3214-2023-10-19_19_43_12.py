a=eval(input())
b=[]
for x in a:
    if x!=0:
        b.append(x)
    else:
        continue
c=len(a)-len(b)
for x in range(c):
    b.extend([0])
print(b)


a=eval(input())
b=[]
for x in a:
    if x==0:
        a.remove(x)
        a.append(x)
    else:
        continue

print(b)


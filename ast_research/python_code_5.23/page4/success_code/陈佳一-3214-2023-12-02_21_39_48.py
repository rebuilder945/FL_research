a=eval(input())
for x in a:
    if x ==0:
        b=a.pop(x)
        a.append(b)
    else:
        continue
print(a)

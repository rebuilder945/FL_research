a = eval(input())
a.sort(reverse=True)
b = []
for x in a:
    if x in a:
        if x not in b:
            b.append(x)
c = ",".join(b)
print(c)
    


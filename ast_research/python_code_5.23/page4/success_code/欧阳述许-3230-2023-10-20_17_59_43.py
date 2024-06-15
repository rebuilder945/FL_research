a=eval(input())
b=sorted(a,reverse=True)
c="".join(map(str,b))
d=()
for x in c:
    if x not in d:
        d.append(x)
print(d)




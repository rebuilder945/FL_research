a=eval(input())
a.sort(reverse=False)
for x in a:
    if x==0:
        a.remove(x)
        a.append(0)
print(a)

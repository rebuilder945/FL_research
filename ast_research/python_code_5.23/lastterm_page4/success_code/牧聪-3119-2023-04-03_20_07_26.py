a=eval(input())
for x in a:
    n=a.index(x,start=-1)
    if x in a[-1:n]:
        a.remove(x)
print(a)


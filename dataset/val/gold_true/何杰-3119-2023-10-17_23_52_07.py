n=eval(input())
n.reverse()
a=[]
for x in n:
    if x in n:
        if x not in a:
            a.append(x)
a.reverse()
print(a)

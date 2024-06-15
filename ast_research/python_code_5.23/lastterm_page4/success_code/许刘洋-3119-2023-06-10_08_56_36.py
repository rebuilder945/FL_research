a=eval(input())
b=[]
a.reverse()
for x in a:
    if x not in b:
        b.insert(0,x)
print(b)


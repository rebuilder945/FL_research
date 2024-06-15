a=eval(input())
a.reverse()
e=[]
for x in a:
    if x not in e:
        e.insert(0,x)
print(e)

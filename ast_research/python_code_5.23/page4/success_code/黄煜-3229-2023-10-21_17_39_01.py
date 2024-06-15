a=eval(input())
b=['']
c=['']
for i in a:
    if i not in b:
        b.insert(0,i)
    else:
        c.insert(0,i)
b.pop()
c.pop()
d=['']
for x in b:
    if x not in c:
        d.insert(0,x)
        d.pop()
        d.sort
        print(d)
    else:
        print("False")

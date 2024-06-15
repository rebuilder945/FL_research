a=input()
b=input()
c=[]
d=[]
if len(a)==len(b):
    for i in a:
        c.append(i)
    c.sort()
    for i in b:
        d.append(i)
    d.sort()
    if c==d:
        print("True")
    else:
        print("False")
else:
    print("false")

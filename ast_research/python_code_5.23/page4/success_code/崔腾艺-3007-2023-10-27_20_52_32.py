a=eval(input())
b,c=eval(input())
d=[]
f=[]
if b<=c:
    for i in range(c-b):
        d.append(a[b+i])
    for x in a:
        if x not in d:
            f.append(x)
        else:
            pass
    print(f)
if b>c or b>len(a) or c>len(a):
    print("error")

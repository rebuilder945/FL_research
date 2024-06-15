a=eval(input())
c=[]
for x in a:
    b=a.count(x)
    if b==1:
        c.append(x)
    else:
        continue
if len(c)==0:
    print("False")
else:
    c.sort()
    print(c)


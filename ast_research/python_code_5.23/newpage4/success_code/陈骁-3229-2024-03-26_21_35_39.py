b=[]
a=eval(input())
for x in a:
    c=a.count(x)
    c=int(c)
    while c==1:
        b.append(x)
        b.sort()
    break
if b==None:
    print("Flase")
else:
    print(b)

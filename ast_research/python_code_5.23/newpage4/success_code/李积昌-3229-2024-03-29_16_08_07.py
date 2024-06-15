a=eval(input())
c=[]
for i in a:
    b=a.count(i)
    if b==1 :
        c.append(i)
if c!=[]:
    c.sort()
    print(",".join(c))
else:
    print("False")

a=eval(input())
b=[]
for x in a:
    c=a.count(x)
    if c==1:
        b.append(str(x))
b.sort()
if b==[]:
    print("False")
else:
    print(",".join(b))


a=eval(input())
c=[]
for x in a:
    b=a.count(x)
    if b==1:
        c.append(x)
c.sort()
if c==[]:
    print("False")
else:
    print(",".join(str(x) for x in c))

        

        

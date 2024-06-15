a=eval(input())
c=[]
for i in a:
    b=a.count(i)
    if b==1 :
        c.append(i)
if c!=[]:
    print(c)
else:
    print("False")

a=eval(input())
a.sort()
b=[]
for i in a:
    number=a.count(i)
    if number==1:
        b.append(i)
if len(b)==0:
    print("False")
    pass
for i in b:
    print(i,end=",")



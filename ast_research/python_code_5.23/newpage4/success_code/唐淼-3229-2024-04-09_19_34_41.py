a=eval(input())
a.sort()
b=[]
for i in a:
    number=a.count(i)
    if number==1:
        b.append(i)
if len(b)==0:
    print("False")
for i in b[0:-1]:
    print(i,end=",")
for i in b[-1]:
    print(i)



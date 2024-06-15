a=eval(input())
b=[]
for x in a:
    c=a.count(x)
    if c==1:
        b.append(x)
b.sort()
if b==[]:
    print("False")
else:
    for i in b: 
        print(i,end=",")

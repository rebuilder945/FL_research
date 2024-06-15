lst=eval(input())
x=[]
for i in lst:
    if lst.count(i)==1:
        x.append(i)
        b=x[-1]
x.sort()
if x==[]:
    print("False")
else:
    for a in x[:-1]:
        print(a,end=",")
        print(b)
        




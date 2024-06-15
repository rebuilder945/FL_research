lst=eval(input())
a=[]
for i in lst:
    if lst.count(i)==1:
        a.append(i)
if a==[]:
    print("False")
else:
    a.sort()
    b=",".join(map(str,a))
    print(b)


l=eval(input())
a=[]
for i in l:
    if l.count(i)==1:
        a.append(i)
a.sort()
if a==[]:
    print("False")
else:
    print(a)

l=eval(input())
a=[]
b=''
for i in l:
    if l.count(i)==1:
        a.append(i)
a.sort()
if a==[]:
    print("False")
else:
    b= ",".join(map(str, a))
    print(b)

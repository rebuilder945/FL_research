a = list(eval(input()))
b=[]
a.sort()
for i in a:
    if a.count(i)==1:
        b.append(i)

if b=[]:
    print("False")
else:
    c=','.join(b)
    print(c)




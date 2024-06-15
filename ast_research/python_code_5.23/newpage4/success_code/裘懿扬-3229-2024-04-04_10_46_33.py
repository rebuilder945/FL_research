ls=list(eval(input()))
a=[]
for i in ls:
    if ls.count(i)==1:
        a.append(i)
if a==[]:
    print("False")
else:
    a.sort()
    c=','.join(str(x) for x in a)
    print(c)



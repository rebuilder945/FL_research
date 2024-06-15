ls=list(eval(input()))
a=[]
for i in ls:
    n=ls.count(i)
    if n==1:
        a.append(i)
if len(a)==0:
    print("False")
else:
    a.sort()
    print(a)

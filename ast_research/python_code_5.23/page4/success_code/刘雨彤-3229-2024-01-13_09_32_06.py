a=eval(input())
ls=[]
for x in a:
    n=a.count(x)
    if n==1:
        ls.append(x)
if ls==0:
    print("False")
else:
    ls.sort()
    b=",".join(str(i) for i in ls)
    print(b)

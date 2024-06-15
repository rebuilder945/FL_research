ls = eval(input())
ls.sort()
x=[]

for i in ls :
    if ls.count(i)==1:
        x.append(i)
if x==[]:
    print(False)
else:
    x=str(x)
    a=x[1:-1:]
    print(a)

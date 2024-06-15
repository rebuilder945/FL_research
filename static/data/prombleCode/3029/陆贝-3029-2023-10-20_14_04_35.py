name=input()
mark=eval(input())
ls=[]
l=len(name)
for i in range(l):
    x=name(i)
    y=mark(i)
    ii=list(x,y)
    ls.append(ii)
print(ls)

name=list(eval(input()))
mark=eval(input())
ls=[]
l=len(mark)
for i in range(l):
    x=name(i)
    y=mark(i)
    ii=list(x,y)
    ls.append(ii)
print(ls)

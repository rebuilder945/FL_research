#name=eval(input())#TypeError: 'str' object is not callable
a=input()
mark=eval(input())
name=a.split(sep=",")
ii=[]
l=len(mark)
for i in range(l):
    a=name[i]
    b=mark[i]
    t=list()
    t.append(a)
    t.append(b)
    ii.append(t)
print(ii)

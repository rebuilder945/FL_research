name=input()
mark=eval(input())
lt=name.split(sep=",")
ii=[]
l=len(mark)
for i in range(l):
    x=name[i]
    y=mark[i]
    a=x+y
    ii.append(a)
print(ii)

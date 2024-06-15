#name=eval(input())#TypeError: 'str' object is not callable
str1=input()
name=[str(n) for n in str1.split(',')]
mark=eval(input())
ls=[]
l=len(mark)
for i in range(l):
    x=name(i)
    y=mark(i)
    ii=list(x,y)
    ls.append(ii)
print(ls)

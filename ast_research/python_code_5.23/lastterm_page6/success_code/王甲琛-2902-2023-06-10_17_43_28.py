n=eval(input())
a=1
b=2
c=b/a
lst1=[c]
for i in range(n):
    a,b=b,a+b
    d=b/a
    lst1.append(d)
print('%.4f'%(sum(lst1)))
    

n=eval(input())
lst=[]
a,b=2,1
for i in range(n):
    c=a/b
    lst.append(c)
    [a,b]=[a+b,a]
print('%.4f'%(sum(lst)))

x=eval(input())
m,n=eval(input())
del x[m:n]
x1=x.copy()
del x1[m:]
if x==x1:
    print('error')
else:
    print(x)

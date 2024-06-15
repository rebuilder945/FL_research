a=eval(input())
a,b=eval(input())
m=max(a,b)
n=min(a,b)
print(m,n)
if m>len(a):
    print('error')
else:
    del a[n:m]
    print(a)


     

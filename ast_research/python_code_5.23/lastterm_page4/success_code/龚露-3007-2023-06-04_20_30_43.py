a=eval(input())
n,m=eval(input())
if 0<=abs((n))<len(a) and 0<=abs((m))<len(a):
    del a[(n):(m)]
else:
    print('error')
print(a)

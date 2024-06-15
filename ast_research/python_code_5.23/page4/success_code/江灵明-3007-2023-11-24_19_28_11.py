a=eval(input())
b,c=input().split(',')
b=int(b)
c=int(c)
if b<=c and c<len(a):
    del a[b:c]
    print(a)
else:
    print('error')

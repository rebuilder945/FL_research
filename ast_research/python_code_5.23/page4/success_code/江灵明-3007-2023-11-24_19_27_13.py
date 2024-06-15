a=eval(input())
b,c=input().split(',')
if b<=c and c<len(a):
    del a[b:c]
    print(a)
else:
    print('error')

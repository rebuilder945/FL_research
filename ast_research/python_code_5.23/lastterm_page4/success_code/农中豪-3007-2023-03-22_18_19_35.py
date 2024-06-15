a=eval(input())
b,c=input().split(',')
b=int(b)
c=int(c)
if b<len(a) and c<len(a):
    if b<c:
        del a[b:c]
        print(a)
    else:
        del a[c+1:b+1]
        print(a)
else:
    print('error')




a=list(map(int,input().split(',')))
b,c=eval(input())
if (b+1)<=len(a):
    for x in range(c):
        b.append(a[b])
    a=a+b
    print(a)
else:
    print('error')




a=list(map(int,input().split(',')))
b,c=eval(input())
d=[]
if(b+1)<=len(a):
    for x in range(c):
        d.append(a[b])
    a=a+d
    print(a)
else:
    print('error')

a=list(map(int,input().split(',')))
b,c=eval(input())
d=[]
if b+1<=len(a):
    d.append(a[b])
    d*c
    print(a+d)
else:
    print('error')


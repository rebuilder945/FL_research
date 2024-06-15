a=list(map(int,input().split(',')))
b,c=eval(input())
if b>len(a)-1:
    print('error')
else:
    d=a[b]
    for x in range(c):
        a.append(c)
    print(a)

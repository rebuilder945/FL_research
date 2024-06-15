a=list(map(int,input().split(',')))
b,c=eval(input())
if b>=-len(a) and b<len(a):
    d=a[b]
    for x in range(c):
        a.append(d)
    print(a)
else:
    print('error')

a=list(eval(input()))
d=a.copy()
b,c=eval(input())
if b<len(a)or -1*b<len(a):
    for i in range(c):
        d.append(a[b])
    print(d)
else:
    print('error')




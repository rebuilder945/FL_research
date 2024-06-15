a=list(eval(input()))
b,c=eval(input())
if b<len(a):
    for i in range(c):
        a.append(a[b])
    print(a)
else:
    print('error')


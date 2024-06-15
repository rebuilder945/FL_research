a=list(eval(input()))
b,c=eval(input())
e='error'
if b>len(a):
    print(e)
else:
    d=a[b]
    for i in range(c):
        a.append(d)
    print(a)

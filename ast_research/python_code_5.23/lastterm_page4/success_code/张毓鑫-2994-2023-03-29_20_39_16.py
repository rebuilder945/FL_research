a=list(eval(input()))
b,c=eval(input())
d=a[b]
if b>len(a):
    print(error)
else:
    for i in range(c):
        a.append(d)
print(a)

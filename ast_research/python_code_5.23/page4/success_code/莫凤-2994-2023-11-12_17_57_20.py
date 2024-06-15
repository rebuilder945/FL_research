a=list(eval(input()))
b,c=eval(input())
if b<len(a)-1:
    d=a[b]
    for x in range(c):
        a.append(d)
    print(a)
else:
    print("error")

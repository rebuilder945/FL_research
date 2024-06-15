a=list(eval(input()))
b,c=eval(input())
if -2<b<=len(a)-1:
    d=a[b]
    a.append(a[b]*c)
    a.remove(d)
    print(a)
else:
    print("error")

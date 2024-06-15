a=list(eval(input()))
b,c=eval(input())
if -2<b<=len(a)-1:
    d=a[b]
    e=[d]
    f=c*e
    a.extend(f)
    print(a)
else:
    print("error")

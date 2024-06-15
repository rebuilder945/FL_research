a=list(eval(input()))
b,c=eval(input())
if -2<b<=len(a)-1:
    c=a[b]
    a.pop(b)
    a.append(b*c)
    print(a)
else:
    print("error")

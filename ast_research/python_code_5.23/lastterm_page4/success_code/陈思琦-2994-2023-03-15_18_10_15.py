a=list(eval(input()))
b,c=eval(input())
if -2<b<=len(a)-1:
    c=a[b]
    a.pop(b)
    for i in range(c):
        a.append(b)
        print(a)
else:
    print("error")

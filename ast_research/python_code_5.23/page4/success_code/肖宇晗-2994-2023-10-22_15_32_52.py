l = list(eval(input()))
n,m = eval(input())
k = len(l)
a = []
if n<k:
    t = l[n]
    a.append(t)
    l.append(a*m)
    print(l)
else:
    print("error")

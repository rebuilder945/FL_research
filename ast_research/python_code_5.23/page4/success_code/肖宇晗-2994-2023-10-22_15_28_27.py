l = eval(input())
n,m = eval(input())
k = len(l)
if n<k:
    t = l[n]
    a = t*m
    l.append(a)
    print(l)
else:
    print("error")

l = list(eval(input()))
n,m = eval(input())
k = len(l)
a = []
if n<k:
    t = l[n]
    a.append(t)
    print(a+l)
else:
    print("error")

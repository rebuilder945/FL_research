l = list(eval(input()))
n, m= eval(input())
e = l[n]
a = []
if n<=len(l):
    a.append(e)
    while a.count(e)<=m-1:
        a.append(e)
    print(l+a)
else:
    print("error")

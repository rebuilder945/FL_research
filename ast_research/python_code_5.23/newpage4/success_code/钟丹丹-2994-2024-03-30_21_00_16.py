l = list(eval(input()))
n, m= eval(input())
a = []
if n<=len(l)-1:
    e = l[n]
    a.append(e)
    while a.count(e)<=m-1:
        a.append(e)
    print(l+a)
else:
    print("error")

v = input()
v = v.split(",")
n,m = eval(input())
a = []
if n >= len(v):
    print("error")
else:
    for i in range(m):
        a.extend([v[n]])
    lst = [ int(x) for x in v+a ]
    print(lst)



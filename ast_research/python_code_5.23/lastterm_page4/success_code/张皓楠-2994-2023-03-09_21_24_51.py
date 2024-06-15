a = eval(input([]))
b,c = eval(input())
d = a[b]
if -len(a)<=b<len(a):
    for i in range(c):
        a.append(d)
    print(a)
else:
    print("error")

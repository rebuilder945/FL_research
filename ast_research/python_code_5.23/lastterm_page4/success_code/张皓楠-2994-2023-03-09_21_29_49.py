a = input().split(",")
b,c = eval(input())
d = a[b]
if -len(a)<=b<len(a):
    for i in range(c):
        a.append(d)
    for i in a:
        i = eval(i)
else:
    print("error")

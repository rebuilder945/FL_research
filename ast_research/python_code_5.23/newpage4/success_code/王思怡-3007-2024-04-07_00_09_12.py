a = list(eval(input()))
b,c = eval(input())
d = []
if b<=c and c<len(a):
    for i in a[b:c]:
        d.append(i)
        for x in d:
            a.remove(x)
    print(a)
else:
    print("error")

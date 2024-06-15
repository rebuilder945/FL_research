a = input().split(',')
e = a.copy()
b,c = eval(input())
d = []
if -len(a) <= b <= len(a)-1:
    for i in range(c):
        e.append(a[b])
    for i in range(len(e)):
        d.append(int(e[i]))
    print(d)
else:
    print('error')

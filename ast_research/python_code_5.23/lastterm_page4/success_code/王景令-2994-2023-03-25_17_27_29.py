a = input().split(',')
b,c = eval(input())
d = []
if -len(a) <= b <= len(a)-1:
    for i in range(c):
        a.append(a[b])
    for i in range(len(a)):
        d.append(int(a[i]))
    print(d)
else:
    print('error')

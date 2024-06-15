a = list(input())
n = int(a[0])
m = int(a[1])
l = int(a[2])
t = [n]
while len(t) < m:
        b = n
        b += l
        t.append(b)
        print(t)

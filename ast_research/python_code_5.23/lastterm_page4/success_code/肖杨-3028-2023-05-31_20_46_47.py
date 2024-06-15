a = list(input())
n = a[0]
m = a[1]
l = a[2]
t = [n]
while len(t) < m:
        b = n
        b += l
        t.append(b)
        print(t)

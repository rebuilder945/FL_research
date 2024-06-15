h = float(input())
N = int(input())
s = []
s.append(h)
for i in range(1,N):
    h = h/2
    s.append(h)
sums = sum(s)
print("%.2f"%sums)


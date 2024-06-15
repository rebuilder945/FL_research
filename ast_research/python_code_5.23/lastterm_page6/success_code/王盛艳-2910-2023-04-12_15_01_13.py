h = int(input())
N = int(input())
sum = h
for x in range(N-1):
    sum += h*0.5**x
print("%.2f"%sum)

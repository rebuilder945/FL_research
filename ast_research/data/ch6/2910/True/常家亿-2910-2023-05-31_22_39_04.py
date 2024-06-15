h = eval(input())
N = eval(input())
s = 0
a = h
for x in range(1,N):
    h = h*0.5
    s += h*2
l = s + a
print("%.2f"%l)

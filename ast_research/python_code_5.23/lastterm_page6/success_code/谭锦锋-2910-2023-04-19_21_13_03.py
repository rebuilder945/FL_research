h = eval(input())
N = eval(input())
x = h
for i in range(N-1):
    x += h*0.5**i
print("%.2f"%(x))

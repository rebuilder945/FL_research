h = eval(input())
N = eval(input())
H = h
for x in range(N-1):
    H += h*0.5**x
print("%.2f"%(H))

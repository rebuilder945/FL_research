h = eval(input())
n = eval(input())
s = h
for i in range(n):
    h = h/2
    s+=h*2
print("%.2f"%(s))

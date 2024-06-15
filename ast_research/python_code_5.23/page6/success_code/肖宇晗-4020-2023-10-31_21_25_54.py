h = eval(input())
n = eval(input())
s = h
for i in range(n):
    h = h*0.5
    s+=h*2
print("%.2f"%(s))

h = eval(input())
n = eval(input())
h1 = h
for x in range (n):
    h = h/2
    h1 = h1 + 2*h
print("%.2f"%(h1-2*h))
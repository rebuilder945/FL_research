h = eval(input())
n = eval(input())
d = [h*0.5**i for i in range(n-1)]
s = h + sum(d)
print("%.2f"%s)

a = eval(input())
b = int(input())
c = []
for i in range(b):
    c.append(a*0.5**i)
h = (sum(c)-a)*2+a
print("%.2f"%h)

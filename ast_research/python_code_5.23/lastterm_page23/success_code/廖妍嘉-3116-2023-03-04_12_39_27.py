(a, b) = eval(input())
(c, d) = eval(input())
e = (a - c)** 2
f = (b - d)** 2
g = (e+f)**(1/2)
h = "%.2f" % (g)
print(h)

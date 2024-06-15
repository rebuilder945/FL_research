h = eval(input())
n = eval(input())
s = h
for x in range(n-1):
    s += h*0.5**x
print('%.2f' % s)

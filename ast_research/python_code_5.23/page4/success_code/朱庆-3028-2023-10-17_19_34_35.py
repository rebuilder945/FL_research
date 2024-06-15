a,b,c = map(eval,input().split(','))
d = []
for x in range(b):
    m = a+c*x
    d.append(m)
print(d)

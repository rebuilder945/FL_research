
a,b,c = map(int,input().split(','))
d = []
for x in range(b):
    m =  a + c*x
    d.append(m)
print(d)


a = eval(input())
n = []
m = []
while a > 0:
    b = a%10
    a = a//10
    n.append(b)
for x in n:
    c = x+5
    m.append(c%10)
for i in range(len(m)):
    m[i],m[-i-1]=m[-i-1],m[i]
o = map(str,m)
s = ''
for y in o:
    s += y
print(s)

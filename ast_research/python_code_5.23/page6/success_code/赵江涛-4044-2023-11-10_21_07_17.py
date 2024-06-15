n = eval(input())
f = 0
for i in range(1,n+1):
    g = i % 10
    s = g % 10
    b = s % 10
    if g**3+s**3+b**3 == i:
        print(i)
        f+=1
if f == 0:
    print('none')

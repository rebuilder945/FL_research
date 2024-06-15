n = input()
m = int(n[0])
p = int(n[2])
if p - m != 3:
    print("illegal input")
else:
    a = m
    b = m+1
    c = m+2
    d = 100*a+10*b+c
    e = 100*a+10*c+b
    f = 100*b+10*a+c
    g = 100*b+10*c+a
    h = 100*c+10*a+b
    i = 100*c+10*b+a
    print(d,e,f,g,h,i)

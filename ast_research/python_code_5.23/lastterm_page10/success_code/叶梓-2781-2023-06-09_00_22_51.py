a = input()
if len(a) != 18:
    print("Error")
else:
    b = int(a[0])
    c = int(a[1])
    d = int(a[2])
    e = int(a[3])
    f = int(a[4])
    g = int(a[5])
    h = int(a[6])
    i = int(a[7])
    j = int(a[8])
    k = int(a[9])
    l = int(a[10])
    m = int(a[11])
    n = int(a[12])
    o = int(a[13])
    p = int(a[14])
    q = int(a[15])
    r = int(a[16])
    b1 = b*7
    c1 = c*9
    d1 = d*10
    e1 = e*5
    f1 = f*8
    g1 = g*4
    h1 = h*2
    i1 = i*1
    j1 = j*6
    k1 = k*3
    l1 = l*7
    m1 = m*9
    n1 = n*10
    o1 = o*5
    p1 = p*8
    q1 = q*4
    r1 = r*2
    a1 = b1+c1+d1+e1+f1+g1+h1+i1+j1+k1+l1+m1+n1+o1+p1+q1+r1
    s = a1%11
    t = (12-s)%11
    if t == 10:
        t = "X"
    else:
        t = t
    if str(t) == str(a[17]):
        print('Correct')
    else:
        print('Wrong')

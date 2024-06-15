num = str(input())
if len(num) != 18:
    print('Error')
else:
    N = [int(i) for i in num[0:17]]
    a = N[0] * 7
    s = N[1] * 9
    d = N[2] * 10
    f = N[3] * 5
    g = N[4] * 8
    h = N[5] * 4
    j = N[6] * 2
    k = N[7] * 1
    l = N[8] * 6
    z = N[9] * 3
    x = N[10] * 7
    c = N[11] * 9
    v = N[12] * 10
    b = N[13] * 5
    m = N[14] * 8
    q = N[15] * 4
    w = N[16] * 2
    tot = a+s+d+f+g+h+j+k+l+z+x+c+v+b+m+q+w
    las = tot % 11
    plas = (12 - las) % 11
    if num[-1] == 'X':
        tlas = 10
        if tlas == plas:
            print('Correct')
        else:
            print('Wrong')
    else:
        if plas == num[-1]:
            print('Correct')
        else:
            print('Wrong')

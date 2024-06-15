a = input()
a = list(a)
if len(a)!=18:
    print('Error')
else:
    b = list(map(int,a[0:len(a)-1]))
    c = [7,9,10,5,8,4,2,1,6,3,7,9,0,5,8,4,2]
    s = 0
    for i in range(0,17):
        s = s+b[i]*c[i]
    n = s%11
    m =(12-n)%11
    if m == 10:
        m = 'X'
    else:
        m = str(m)
    if m == a[17]:
        print('Correct')
    else:
        print('Wrong')


    


def f(x,y):
    p=True
    q=(12-x)%11
    if q<10 and str(q) != y[17]:
        p = False
    if q==10 and y[17] != 'X':
        p = False
    return p
            

x=input()
if len(x) != 18:
    print('Error')
else:
    num=int(x[0])*7+int(x[1])*9+int(x[2])*10+int(x[3])*5+int(x[4])*8+int(x[5])*4+int(x[6])*2+int(x[7])+int(x[8])*6+int(x[9])*3+int(x[10])*7+int(x[11])*9+int(x[12])*10+int(x[13])*5+int(x[14])*8+int(x[15])*4+int(x[16])*2
    yu=num % 11
    r = f(yu,x)
    if r == True:
        print('Correct')
    else:
        print('Wrong')

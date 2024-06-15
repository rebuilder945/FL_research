a=input()
if len(a)!=18:
    print('Error')
else:
    b=eval(a[0])*7+eval(a[1])*9+eval(a[2])*10+eval(a[3])*5+eval(a[4])*8+eval(a[5])*4+eval(a[6])*2+eval(a[7])+eval(a[8])*6+eval(a[9])*3+eval(a[10])*7+eval(a[11])*9+eval(a[12])*10+eval(a[13])*5+eval(a[14])*8+eval(a[15])*4+eval(a[16])*2
    n=b%11
    if n==0:
        m=1
    elif n==1:
        m=0
    elif n==2:
        m='X'
    else:
        m=12-n
    # print(b,n,m,eval(a[17]))
    if m==eval(a[17]):
        print('Correct')
    else:
        print('Wrong')

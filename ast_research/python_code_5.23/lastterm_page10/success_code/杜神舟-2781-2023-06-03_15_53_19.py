a=input()
ls1=[0,1,2,3,4,5,6,7,8,9,10]
ls3=[1,0,'x',9,8,7,6,5,4,3,2]
if len(a)==18:
    b=int(a[0])*7+int(a[1])*9+int(a[2])*10+int(a[3])*5+int(a[4])*8+int(a[5])*4+int(a[6])*2+int(a[7])+int(a[8])*6+int(a[9])*3+int(a[10])*7+int(a[11])*9+int(a[12])*10+int(a[13])*5+int(a[14])*8+int(a[15])*4+int(a[16])*2
    b=b%11
    c=int((12-b)%11)
    if a[17]==str(ls3[b]):
        print('Correct')
    else:
        print('Wrong')
else:
    print('Error')



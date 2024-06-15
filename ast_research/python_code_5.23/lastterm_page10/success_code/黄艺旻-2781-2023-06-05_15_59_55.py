def yan(a):
    var=['0','1','2','3','4','5','6','7','8','9','10']
    var_id=['1','0','X','9','8','7','6','5','4','3','2']
    s=int(a[0])*7+int(a[1])*9+int(a[2])*10+int(a[3])*5+int(a[4])*8+int(a[5])*4+int(a[6])*2+int(a[7])*1+int(a[8])*6+int(a[9])*3+int(a[10])*7+int(a[11])*9+int(a[12])*10+int(a[13])*5+int(a[14])*8+int(a[15])*4+int(a[16])*2
    y=s%11
    if var_id[y]==a[-1]:
        print('Correct')
    else:
        print('Wrong')
a=input()
if len(a)!=18:
    print('Error')
else:
    yan(a)

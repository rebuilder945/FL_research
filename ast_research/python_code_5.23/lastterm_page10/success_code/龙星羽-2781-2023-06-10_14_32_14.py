s=input()
if len(s) == 18:
    a=int(s[0])*7+int(s[1])*9+int(s[2])*10+int(s[3])*5+int(s[4])*8+int(s[5])*4+int(s[6])*2+int(s[7])*1+int(s[8])*6+int(s[9])*3+int(s[10])*7+int(s[11])*9+int(s[12])*10+int(s[13])*5+int(s[14])*8+int(s[15])*4+int(s[16])*2
    a1=a%11
    ls=[1,0,"X",9,8,7,6,5,4,3,2]
    if ls[a1]==s[17]:
        print('Correct')
    else:
        print('Wrong')
else:
    print('Error')







s=str(input())
if len(s)!=18:
    print('Error')
else:
    m=int(s[0])*7+int(s[1])*9+int(s[2])*10+int(s[3])*5+int(s[4])*8+int(s[5])*4+int(s[6])*2+int(s[7])*1+int(s[8])*6+int(s[9])*3+int(s[10])*7+int(s[11])*9+int(s[12])*10+int(s[13])*5+int(s[14])*8+int(s[15])*4+int(s[16])*2
    yu=(12-m)%11
    if s[17]=='X':
        if yu==10:
            print('Correct')
        else:
            print('Wrong')
    else:
        if int(s[17])==yu:
            print('Correct')
        else:
            print('Wrong')
            


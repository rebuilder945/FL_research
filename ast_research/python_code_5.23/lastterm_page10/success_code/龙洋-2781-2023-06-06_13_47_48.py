id=input()
if len(id)==18:
    x=int(id[0])*7+int(id[1])*9+int(id[2])*10+int(id[3])*5+int(id[4])*8+int(id[5])*4+int(id[6])*2+int(id[7])*1+int(id[8])*6+int(id[9])*3+int(id[10])*7+int(id[11])*9+int(id[12])*10+int(id[13])*5+int(id[14])*8+int(id[15])*4+int(id[16])*2
    n=x%11
    m=(12-n)%11
    if m==10 or id[-1]=='X':
        if id[-1]!='X':
            print('Wrong')
        else:
            print('Correct')
    else:
        if m==eval(id[-1]):
            print('Correct')
        else:
            print('Wrong')
else:
    print('Error')


s=list(input())

if len(s)!=18:
    print("Error")
else:
    a=int(s[0])*7+int(s[1])*9+int(s[2])*10+int(s[3])*5+int(s[4])*8+int(s[5])*4+int(s[6])*2+int(s[7])*1+int(s[8])*6+int(s[9])*3+int(s[10])*7+int(s[11])*9+int(s[12])*10+int(s[13])*5+int(s[14])*8+int(s[15])*4+int(s[16])*2
    
    b=int(a)%11
    m=(12-b)%11
    if m==s[-1]:
        print("Correct")
    elif b==2 and s[-1]=='X':
        print("Correct")
    else:
        print("Wrong")

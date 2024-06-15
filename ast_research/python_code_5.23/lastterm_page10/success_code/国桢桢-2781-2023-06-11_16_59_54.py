s = input()
if len(s)!=18:
    print("Error")
else:
    b = int(s[0])*7+int(s[1])*9+int(s[2])*10+int(s[3])*5+int(s[4])*8+int(s[5])*4+int(s[6])*2+int(s[7])*1+int([8])*6+int(s[9])*3+int(s[10])*7+int(s[11])*9+int(s[12])*10+int(s[13])*5+int(s[14])*8+int(s[15])*4+int(s[16])*2
    m = s[-1]
    n = b%11
    if m!="X":
        m = int(m)
        if m ==(12-n)%11:
            print("Correct")
        else:
            print("Wrong")
    else:
        m=10
        if m==(12-n)%11:
            print("Corrrect")
        else:
            print("Wrong")

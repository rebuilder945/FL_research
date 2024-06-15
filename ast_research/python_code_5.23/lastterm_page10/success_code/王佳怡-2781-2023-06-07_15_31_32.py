a1=input()
if len(a1)!=18:
    print("Error")
else:
    b=int(a1[0])*7+int(a1[1])*9+int(a1[2])*10+int(a1[3])*5+int(a1[4])*8+int(a1[5])*4+int(a1[6])*2+int(a1[7])*1+int(a1[8])*6+int(a1[9])*3+int(a1[10])*7+int(a1[11])*9+int(a1[12])*10+int(a1[13])*5+int(a1[14])*8+int(a1[15])*4+int(a1[16])*2   
    n=b%11
    m=a1[-1]
    if m!="X":
        m=int(m)
        if m==(12-n)%11:
            print("Correct")
        else:
            print("Wrong")
    else:
        m=10
        if m==(12-n)%11:
            print("Correct")
        else:
            print("Wrong")

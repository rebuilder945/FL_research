b = input()
if len(b)==18:
    c = int(b[0])*7+int(b[1])*9+int(b[2])*10+int(b[3])*5+int(b[4])*8+int(b[5])*4+int(b[6])*2+int(b[7])+int(b[8])*6+int(b[9])*3+int(b[10])*7+int(b[11])*9+int(b[12])*10+int(b[13])*5+int(b[14])*8+int(b[15])*4+int(b[16])*2
    n = c%11
    h = b[17]
    if h==str(((12-n)%11)):
        print("Correct")
    elif h == "X":
        if n==2:
            print("Correct")
        else:
            print("Wrong")
    else:
        print("Wrong")
else:
    print("Error")

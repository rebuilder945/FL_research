icard = input()
if len(icard)==18:
    sum=int(icard[0])*7+int(icard[1])*9+int(icard[2])*10+int(icard[3])*5+int(icard[4])*8+int(icard[5])*4+int(icard[6])*2+int(icard[7])*1+int(icard[8])*6+int(icard[9])*3+int(icard[10])*7+int(icard[11])*9+int(icard[12])*10+int(icard[13])*5+int(icard[14])*8+int(icard[15])*4+int(icard[16])*2
    n =sum%11
    m=(12-n)%11
    if icard[17]=="X":
        if m==10:
            print("Correct")
        else:
            print("Wrong")
    elif icard[17]!="X":
        if icard[17]==m:
            print("Correct")
        else:
            print("Wrong")
else:
    print("Error")    
    



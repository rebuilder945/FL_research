a=list(input())
if len(a)!=18:
    print("Error")
elif len(a)==18:
    k=int(a[0])*7+int(a[1])*9+int(a[2])*10+int(a[3])*5+int(a[4])*8+int(a[5])*4+int(a[6])*2+int(a[7])+int(a[8])*6+int(a[9])*3+int(a[10])*7+int(a[11])*9+int(a[12])*10+int(a[13])*5+int(a[14])*8+int(a[15])*4+int(a[16])*2
    n=k%11
    m=(12-n)%11

    if m==10:
        m="X"
        if a[-1]!=m:
            print("Wrong")
        else:
            print("Correct")
    elif int(a[17])==m:
        print("Correct")
    else:
        print("Wrong")

    

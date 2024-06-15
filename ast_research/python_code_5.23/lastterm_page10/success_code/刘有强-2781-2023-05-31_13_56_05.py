a=input()
if len(a) != 18:
    print("Error")
else:
    ss=(int(a[0])*7)+(int(a[1])*9)+(int(a[2])*10)+(int(a[3])*5)+(int(a[4])*8)+(int(a[5])*4)+(int(a[6])*2)+(int(a[7])*1)+(int(a[8])*6)+(int(a[9])*3)+(int(a[10])*7)+(int(a[11])*9)+(int(a[12])*10)+(int(a[13])*5)+(int(a[14])*8)+(int(a[15])*4)+(int(a[16])*2)
    b=ss%11
    if b == 0 and a[-1]=='1':
        print("Correct")
    if b == 1 and a[-1]=='0':
        print("Correct")
    if b == 2 and a[-1]=='X':
        print("Correct")
    if b == 3 and a[-1]=='9':
        print("Correct")
    if b == 4 and a[-1]=='8':
        print("Correct")
    if b == 5 and a[-1]=='7':
        print("Correct")
    if b == 6 and a[-1]=='6':
        print("Correct")
    if b == 7 and a[-1]=='5':
        print("Correct")
    if b == 8 and a[-1]=='4':
        print("Correct")
    if b == 9 and a[-1]=='3':
        print("Correct")
    if b == 10 and a[-1]=='2':
        print("Correct")
    else:
        print("Error")


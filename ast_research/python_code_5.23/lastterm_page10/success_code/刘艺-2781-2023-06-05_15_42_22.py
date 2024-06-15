a = input()
ls1 = []
if len(a) != 18:
    print("Error")
elif len(a)==18:
    for i in range(0,len(a)-1):
        ls1.append(a[i])
    sum = int(ls1[0])*7+int(ls1[1])*9+int(ls1[2])*10+int(ls1[3])*5+int(ls1[4])*8+int(ls1[5])*4+int(ls1[6])*2+int(ls1[7])*1+int(ls1[8])*6+int(ls1[9])*3+int(ls1[10])*7+int(ls1[11])*9+int(ls1[12])*10+int(ls1[13])*5+int(ls1[14])*8+int(ls1[15])*4+int(ls1[16])*2
    n = sum%11
    m = (12-n)%11
    if a[-1] == "X":
        b = 2
    if m in [0,1,10,3,4,5,6,7,8,9]:
        if m == int(a[-1]):
            print("Correct")
        else:
            print("Wrong")
    if m==2:
        if m == 2:
            print("Correct")
        else:
            print("Wrong")

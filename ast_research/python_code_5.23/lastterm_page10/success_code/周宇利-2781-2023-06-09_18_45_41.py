n=list(input())
lastnumber=["0","1","2","3","4","5","6","7","8","9","10"]
Y=["1","0","X","9","8","7","6","5","4","3","2","1"]
if len(n)!=18:
    print("Error")
else:
    a=int(n[0])*7+int(n[1])*9+int(n[2])*10+int(n[3])*5+int(n[4])*8+int(n[5])*4+int(n[6])*2+int(n[7])*1+int(n[8])*6+int(n[9])*3+int(n[10])*7+int(n[11])*9+int(n[12])*10+int(n[13])*5+int(n[14])*8+int(n[15])*4+int(n[16])*2
    c=a%11
    for i in lastnumber:
        if c==int(i):
            if n[17]==Y[lastnumber.index(i)]:
                print("Correct")
            else:
                print("Wrong")

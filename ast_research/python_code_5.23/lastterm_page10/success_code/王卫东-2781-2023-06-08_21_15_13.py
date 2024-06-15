n=list(input())
s=0
if len(n)!=18:
    print("Error")
else:
    a=(int(n[0])*7+int(n[1])*9+int(n[2])*10+int(n[3])*5+int(n[4])*8+int(n[5])*4+int(n[6])*2+int(n[7])*1+int(n[8])*6+int(n[9])*3+int(n[10])*7+int(n[11])*9+int(n[12])*10+int(n[13])*5+int(n[14])*8+int(n[15])*4+int(n[16])*2)%11
    m=(12-a)%11
if n[-1]=="X":
    n[-1]=10
if n[-1]==m:
    print("Correct")
else:
    print("Wrong")               

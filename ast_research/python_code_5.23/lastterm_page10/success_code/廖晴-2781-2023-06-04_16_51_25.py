
num=list(input())
su=int(num[0])*7+int(num[1])*9+int(num[2])*10+int(num[3])*5+int(num[4])*8+int(num[5])*4+int(num[6])*2+int(num[7])+int(num[8])*6+int(num[9])*3+int(num[10])*7+int(num[11])*9+int(num[12])*10+int(num[13])*5+int(num[14])*8+int(num[15])*4+int(num[16])*2
yushu=su%11
m=(12-yushu)%11
if len(num)!=18:
    print("Error")
else:
    if int(num[17])==m:
        print("Correct")
    else:
        print("Wrong")

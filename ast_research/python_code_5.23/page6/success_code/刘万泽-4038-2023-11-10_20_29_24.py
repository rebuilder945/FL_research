zifuchuan=str(input())
yingwenzimu,shuzi,kongge,qita=0,0,0,0
for i in zifuchuan:
    if "a"<=i<="z" or "A"<=i<="Z":
        yingwenzimu+=1
    elif "0"<=i<="9":
        shuzi+=1
    elif i==" ":
        kongge+=1
    else:
        qita+=1
print(yingwenzimu,kongge,shuzi,qita)                    


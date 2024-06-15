str1=input()
yingwen=0
kongge=0
shuzi=0
qita=0
for i in str1:
    if "A" <= i <= "Z" or 'a' <= i <= "z":
        yingwen+=1
    elif i == " ":
        kongge+=1
    elif "0" <= i <= "9":
        shuzi+=1
    else:
        qita+=1
print("%d"%yingwen,"%d"%kongge,"%d"%shuzi,"%d"%qita)

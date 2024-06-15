zifu=input()
zimu=0
kongge=0
shuzi=0
qita=0
for i in zifu:
    if 'a'<=i<='z' or 'A'<=i<='Z' :
        zimu+=1
    elif i==' ':
        kongge+=1
    elif '0'<=i<='9':
        shuzi+=1
    else:
        qita+=1
print(zimu,kongge,shuzi,qita)

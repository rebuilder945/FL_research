lst1=list(input())
shuzi=0
zimu=0
kongge=0
qita=0
for i in lst1:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        zimu+=1
    elif ord(i)>=48 and ord(i)<=57:
        shuzi+=1
    elif i==' ':
        kongge+=1
    else:
        qita+=1
print("{} {} {} {}".format(zimu,kongge,shuzi,qita))


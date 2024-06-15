list1=list(input())
shuzi=0
zimu=0
kongge=0
qita=0
for i in list1:
    if type(i)==int or type(i)==float:
        shuzi+=1
    elif type(i)==str:
        zimu+=1
    elif i==' ':
        kongge+=1
    else:
        qita+=1
print("{} {} {} {}".format(zimu,kongge,shuzi,qita))
    


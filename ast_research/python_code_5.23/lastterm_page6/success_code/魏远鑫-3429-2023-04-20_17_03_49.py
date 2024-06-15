n=input().split()
yingwen=0
space=len(n)-1
shuzi=0
qita=0
for i in n:
    for x in i:
        if 'a'<= x <= 'z':
            yingwen+=1
        elif '0'<= x <='9':
            shuzi+=1
        else:
            qita+=1
print(yingwen,space,shuzi,qita,end=" ")






    



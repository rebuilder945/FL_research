str1=input()
name=[str(n) for n in str1.split(',')]
grade=eval(input())
long=len(name)
jishu=0
x2=[]
while long>0:
    x1=[]
    x1.append(name[jishu])
    x1.append(grade[jishu])
    x2.append(x1)
    jishu+=1
    long-=1
jishu1=0

eva=[]
for x11 in x2:
    jishu2=0
    for x12 in x2:
        if x12[1]>x11[1]:
            eva=x2[jishu1]
            x2[jishu1]=x2[jishu2]
            x2[jishu2]=eva
        jishu2+=1
    jishu1+=1
print(x2)

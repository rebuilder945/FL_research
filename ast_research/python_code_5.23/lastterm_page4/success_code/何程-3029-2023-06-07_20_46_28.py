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
print(x2)

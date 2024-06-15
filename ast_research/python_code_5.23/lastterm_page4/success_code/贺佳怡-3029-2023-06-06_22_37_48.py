str1=input()
name=[str(n) for n in str1().split('')]
grade=eval(input())
a=0
b=len(name)
x1=[]
while b>0:
    x2=[]
    x2.append(name[a])
    x2.append(grade[a])
    x1.append(x2)
    a+=1
    b-=1
print(x1)



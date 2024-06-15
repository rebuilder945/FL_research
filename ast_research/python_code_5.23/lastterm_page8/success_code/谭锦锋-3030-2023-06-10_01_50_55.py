str1 = input()
name=[str(n) for n in str1.split(",")]
grade = eval(input())
long = len(name)
s = 0
x2=[]
while long>0:
    x1=[]
    x1.append(name[s])
    x1.append(grade[s])
    x2.append(x1)
    s+=1
    long-=1
s1 = 0
eva=[]
for i in x2:
    s2 = 0
    for j in x2:
        if j[1]>i[1]:
            eva=x2[s1]
            x2[s1]=x2[s2]
            x2[s2]=eva
        s2+=1
    s1+=1
print(x2)

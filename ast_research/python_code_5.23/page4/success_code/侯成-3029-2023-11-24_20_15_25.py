test=input()
name=[str(x) for x in test.split(",")]
grade=eval(input())
long=len(name)
standard=0
a=[]
while long>0:
    b=[]
    b.append(name[standard])
    b.append(grade[standard])
    a.append(b)
    standard+=1
    long-=1
print(a)


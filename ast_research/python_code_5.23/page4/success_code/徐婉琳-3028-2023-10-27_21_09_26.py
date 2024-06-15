


c=input("姓名：").split(',')
b=eval(input("成绩："))

m=[]
for h in range(len(c)):
    m.append([c[h],b[h]])
print(m)


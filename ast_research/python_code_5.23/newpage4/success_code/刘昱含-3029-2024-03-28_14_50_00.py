name=str(input()).split(",")
grade=eval(input())
qian=[]
for x in range(len(name)):
    qian.append([name[x],grade[x]])
print(qian)

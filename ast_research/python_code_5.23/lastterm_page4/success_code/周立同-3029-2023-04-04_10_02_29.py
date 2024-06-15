names=input().split(",")
grade=eval(input())
fin=[]
for i in range(0,len(grade)):
    pipei=[names[i],grade[i]]
    fin.append(pipei)
print(fin)

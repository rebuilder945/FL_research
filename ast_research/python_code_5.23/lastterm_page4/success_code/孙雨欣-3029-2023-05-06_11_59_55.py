name=input().split(',')
grade=eval(input())
ls3=[]
ls4=[]
for i in range(len(name)):
    ls3=[name[i],grade[i]]
    ls4.append(ls3)
print(ls4)

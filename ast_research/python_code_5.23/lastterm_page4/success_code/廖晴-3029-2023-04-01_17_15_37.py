name=input().split(',')
grade=eval(input())
s=[]
for i in range(len(name)):
    s.append([name[i],grade[i]])
print(s)

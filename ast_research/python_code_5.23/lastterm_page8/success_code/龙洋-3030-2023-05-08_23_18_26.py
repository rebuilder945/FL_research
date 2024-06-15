name=input().split(',')
grade=input().split(',')
li1=[[x,0]for x in name]
num=len(name)
for x in range(num):
    li1[x][1]=int(grade[x])
li1.sort(key=lambda x:x[1])
print(li1)

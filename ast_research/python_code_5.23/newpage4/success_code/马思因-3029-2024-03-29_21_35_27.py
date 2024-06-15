name=input().split(",")
grade=eval(input())
list=[]
for i in range(len(name)):
    a=[name[i],grade[i]]
    list.append(a)
print(list)

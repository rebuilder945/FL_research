a=input()
name=a.split(",")
grade=eval(input())
list=[]
for i in range(len(name)):
    c=[name[i],grade[i]]
    list.append(c)
print(list)

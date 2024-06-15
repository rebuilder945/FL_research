name=input().split(",")
#grade=list(map(int,input().split(",")))
grade = eval(input())
list1=[]
for i in range(len(name)):
    a=[name[i],grade[i]]
    list1.append(a)
print(list1)    

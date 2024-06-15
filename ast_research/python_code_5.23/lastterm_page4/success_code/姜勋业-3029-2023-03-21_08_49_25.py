names=input().split(",")
name=list(names)
gpa=eval(input())
a2=[]
for i in range(len(gpa)):
    a1=[name[i],gpa[i]]
    a2.append(a1)
print(a2)

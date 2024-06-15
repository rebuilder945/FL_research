names=input().split(",")
name=list(names)
gpa=eval(input())
ls1=[]
ls=[]
for i in range(len(gpa)):
    ls1=[name(i),gpa(i)]
    ls.append(ls1)
print(ls)

sname=list(input().split(","))
grade=list(eval(input()))
dlist=[]
l=len(grade)
for i in range(0,l):
    dlist.append([sname[i],grade[i]])
print(dlist) 

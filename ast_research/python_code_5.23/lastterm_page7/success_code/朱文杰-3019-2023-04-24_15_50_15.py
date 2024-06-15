ls=input().split()
for i in range(1,4):
    ls[i]=int(ls[i])
ls2=ls[1:4]
stu={}
stu["name"]=ls[0]
stu["english"]=ls2[0]
stu["python"]=ls2[1]
stu["math"]=ls2[2]
stu["avg"]=(ls2[0]+ls2[1]+ls2[2])/len(ls2)
gra=[stu["english"],stu["python"],stu["math"]]
gra.sort(reverse=True)
print(stu["name"],"%.2f"%(gra[0]),"%.2f"%(gra[1]),"%.2f"%(gra[2]),"%.2f"%(stu["avg"]))

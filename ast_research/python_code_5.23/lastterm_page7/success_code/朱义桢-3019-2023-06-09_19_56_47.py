a=input().split()
stu={}
stu['name']=a[0]
stu['english']=int(a[1])
stu["python"]=int(a[2])
stu["math"]=int(a[3])
stu["avg"]=(stu["english"]+stu["math"]+stu["python"])/3
b=[stu["english"],stu["math"],stu["python"]]
b.sort(reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(stu["name"],b[0],b[1],b[2],stu["avg"]))

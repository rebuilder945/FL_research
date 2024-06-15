ls=input().split()
stu={}
stu["name"]=ls[0]
stu["english"]=eval(ls[1])
stu["python"]=eval(ls[2])
stu["math"]=eval(ls[3])
average=(stu['english']+stu["python"]+stu["math"])/3
stu["avg"]=average
ls=list(stu.values())
ls.pop(0)
ls.pop()
ls.sort(reverse=True)
print(stu["name"],end=' ')
ls.append(average)
for i in ls:
    print("%.2f"%(i),end=' ')


str1=input()
ls=str1.split(" ")
stu={}
stu["names"]=ls[0]
stu["english"]=eval(ls[1])
stu["python"]=eval(ls[2])
stu["math"]=eval(ls[3])
sum=eval(ls[1])+eval(ls[2])+eval(ls[3])
avg=sum/3
stu["avg"]=avg
for i in stu:
    if type(stu[i])==str:
        print(stu[i],end=" ")
    else:
        print("%.2f"%(stu[i]),end=" ")

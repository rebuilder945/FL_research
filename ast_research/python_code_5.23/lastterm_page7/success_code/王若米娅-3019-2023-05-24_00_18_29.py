str1=input()
ls=str1.split(" ")
stu={}
stu.get("names",ls[0])
stu.get("english",eval(ls[1]))
stu.get("python",eval(ls[2]))
stu.get("math",eval(ls[3]))
sum=eval(ls[1])+eval(ls[2])+eval(ls[3])
avg=sum/3
stu.get("avg",avg)
for i in stu:
    if type(stu[i])==string:
        print(stu[i],end=" ")
    else:
        print("%.2f"%(stu[i]),end=" ")

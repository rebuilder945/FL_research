s,a,b,c=input().split()
a,b,c=eval(a),eval(b),eval(c)
stu={"name":s,"english":a,"python":b,"math":c}
lst=[]
for k,v in stu.items():
    if k!="name":
        lst.append(v)
lst.sort()
stu["avg"]=(a+b+c)/3
print(stu["name"],end=' ')
for i in range(len(lst)):
    print("%.2f"%(lst[i]),end=' ')
print("%.2f"%(stu["avg"]))

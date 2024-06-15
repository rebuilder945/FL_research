a,b,c,d=eval(input())
stu={"name":a,"english":b,"python":c,"math":d}
e=(b+c+d)/3
stu["avg":e]
print("{} {} {} {} {}".format(a,"%.2f"%b,"%.2f"%c,"%.2f"%d,"%.2f"%e))

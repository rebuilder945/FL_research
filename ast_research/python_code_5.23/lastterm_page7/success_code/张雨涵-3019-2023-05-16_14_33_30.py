name,e,p,m=input().split()
stu={"name":name,"english":e,"python":p,"math":m}
e,p,m=eval(e),eval(p),eval(m)
av = (e+p+m)/3
ls = [e,p,m]
ls.sort()
ls.reverse()
print(name," ".join("%.2f"%id for id in ls),"%.2f"%av )

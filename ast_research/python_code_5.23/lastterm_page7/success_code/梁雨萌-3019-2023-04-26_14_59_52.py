name,eng,math,py=input().split()
eng=int(eng)
math=int(math)
py=int(py)
dic={"name":name,"eng":eng,"math":math,"py":py,}
dic["avg"]=(eng+math+py)/3
lis=[eng,math,py]
lis.reverse()
print(name,"%.2f %.2f %.2f"%(lis[0],lis[1],lis[2]),dic["avg"])


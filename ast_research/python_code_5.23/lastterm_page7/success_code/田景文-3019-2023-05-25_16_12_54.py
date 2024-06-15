stu = {}
ls = list(map(str,input().split()))
ls[1],ls[2],ls[3] = eval(ls[1]),eval(ls[2]),eval(ls[3])
stu["name"] = ls[0]
stu["english"] = ls[1]
stu["python"] = ls[2]
stu["masth"] = ls[3]
stu["avg"] = (ls[1] + ls[2] + ls[3])/3
del ls[0]
ls.sort(reverse=True)
ls.insert(0,stu["name"])
ls.append(stu["avg"])
print("%s %.2f %.2f %.2f %.2f"%(ls[0],ls[1],ls[2],ls[3],ls[4]))

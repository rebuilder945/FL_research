# lst=input().split(" ")
# lst[1]=eval(lst[1])
# lst[2]=eval(lst[2])
# lst[3]=eval(lst[3])
# stu={}
# stu["name"]=lst[0]
# stu['english']=lst[1]
# stu['python']=lst[2]
# stu['math']=lst[3]
# avg=(lst[1]+lst[2]+lst[3])/3
# studp=stu.copy()
# stu['avg']=avg
# studp.pop('name')
# lst2=list(studp.items())
# lst2.sort(key=lambda x:x[1],reverse=True)
# print(stu['name'],"%.2f %.2f %.2f %.2f"%(lst2[0][1],lst2[1][1],lst2[2][1],stu['avg']))


lst=input().split(" ")
lst[1]=eval(lst[1])
lst[2]=eval(lst[2])
lst[3]=eval(lst[3])
stu={}
stu['english']=lst[1]
stu['python']=lst[2]
stu['math']=lst[3]
avg=(lst[1]+lst[2]+lst[3])/3
lst2=list(stu.items())
lst2.sort(key=lambda x:x[1],reverse=True)
print(lst[0],"%.2f %.2f %.2f %.2f"%(lst2[0][1],lst2[1][1],lst2[2][1],avg))

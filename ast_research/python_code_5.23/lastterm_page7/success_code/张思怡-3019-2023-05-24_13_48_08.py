stu={"name":"Zhang","english":80,"python":90,"math":100}
a=input().split(" ")
stu['name']=a[0]
stu['english']=eval(a[1])
stu['python']=eval(a[2])
stu['math']=eval(a[3])
stu['avg']=(eval(a[1])+eval(a[2])+eval(a[3]))/3
# print(stu)
list1=[]
list2=[]
for k,v in stu.items():
    list1.append([k,v])
for i in range(1,4):
    list2.append(list1[i])
list2.sort(key=lambda x:x[1],reverse=True)
# print(stu)
# print(list1)
# print(list2)
jieguo=[]
jieguo.append(a[0])
for i in range(0,3):
    jieguo.append(list2[i][1])
jieguo.append(list1[4][1])
print(str(jieguo))

print("%s %.2f %.2f %.2f %.2f"%(jieguo[0],jieguo[1],jieguo[2],jieguo[3],jieguo[4]))

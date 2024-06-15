a=input().split()
stu={}
stu["name"]=a[0]
del a[0]
a[0]=int(a[0])
a[1]=int(a[1])
a[2]=int(a[2])
a.sort(reverse=True)
avg=float(sum(a)/len(a))
a.append(avg)
print(stu["name"],"%.2f"%(int(a[0])),"%.2f"%(int(a[1])),"%.2f"%(int(a[2])),"%.2f"%(int(a[3])))


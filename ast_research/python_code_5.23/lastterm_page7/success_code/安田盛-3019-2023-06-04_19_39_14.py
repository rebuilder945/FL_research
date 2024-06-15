name,english,python,math=map(str,input().split())
stu=[]
stu.append(int(english))
stu.append(int(python))
stu.append(int(math))
avg=sum(stu)/len(stu)
stu.sort( reverse=True)
stu.append(avg)
print("%s %.2f %.2f %.2f %.2f"%(name,stu[0],stu[1],stu[2],avg))



            





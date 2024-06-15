n=input().split( )
stu={"name":n[0],"english":n[1],"python":n[2],"math":n[3]}
avg=int(n[1]+n[2]+n[3])/3
stu['avg']=avg
nums=[int(n[1]),int(n[2]),int(n[3])]
nums.sort(reverse=True)
print(n[0],"%.2f %.2f %.2f %.2f"%(nums[0],nums[1],nums[2],stu["avg"]))


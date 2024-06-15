m=input().split(" ")
stu=dict((("name",m[0]),("english",m[1]),("python",m[2]),("math",m[3])))
stu["avg"]=(int(m[1])+int(m[2])+int(m[3]))/3
nums=[int(m[1]),int(m[2]),int(m[3])]
nums.sort(reverse=True)
print(m[0],"%.2f %.2f %.2f %.2f"%(nums[0],nums[1],nums[2],nums[3]))





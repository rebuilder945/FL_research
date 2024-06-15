m=input().split(" ")
stu=dict((("name",m[0]),("english",m[1]),("python",m[2]),("math",m[3])))
stu["avg"]=(int(m[1])+int(m[2])+int(m[3]))/3
a=("%.2f"%stu["avg"])
nums=[int(m[1]),int(m[2]),int(m[3])]
nums.sort(reverse=True)
print(m[0],"{} {} {} {}".format(float(nums[0]),float(nums[1]),float(nums[2]),float(a))


nums=input().split(" ")
x=nums[0]
del nums[0]
nums=map(int,nums)
nums.sort()
avg=sum(nums)/3
nums.append(avg)
a=round(nums[0],2)
b=round(nums[1],2)
c=round(nums[2],2)
d=round(nums[3],2)
let=[]
let.append(x)
let.append(a)
let.append(b)
let.append(c)
let.append(d)
for i in let:
    print(i,end="")




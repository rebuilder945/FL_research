nums=input().split(" ")
x=nums[0]
del nums[0]
k=int(nums[0])
v=int(nums[1])
g=int(nums[2])
nums.sort()
avg=(k+v+g)/3
nums.append(avg)
j=nums[3]
round(k,2)
round(v,2)
round(g,2)
round(j,2)
let=[]
let.append(x)
let.append(k)
let.append(v)
let.append(g)
let.append(j)
for i in let:
    print(i,end=" ")




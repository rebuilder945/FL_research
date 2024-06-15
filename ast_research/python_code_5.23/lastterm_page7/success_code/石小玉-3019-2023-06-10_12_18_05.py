nums=input().split(" ")
x=nums[0]
del nums[0]
k=int(nums[0])
v=int(nums[1])
g=int(nums[2])
nums.sort()
avg=(k+v+g)/3
nums.append(avg)
a=round(k,2)
b=round(v,2)
c=round(g,2)
d=round(nums[3],2)
let=[]
let.append(x)
let.append(a)
let.append(b)
let.append(c)
let.append(d)
for i in let:
    print(i,end="")




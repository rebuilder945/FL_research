n = int(input())
nums=range(1, n+1)
sums2=[]
m=nums[0]
for i in range(len(nums)-1):
     sums2.append(nums[i+1])
sums2.append(m)
print(sums2)

names=input().split(",")
nums=eval(input())
sums1=list(names)
sums2=[]
for i in range(len(nums)):
    sums3=(sums1[i],nums[i])
    sums2.append(list(sums3))
print(sums2)

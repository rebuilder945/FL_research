nums=eval(input())
nums.sort()
k=sorted(nums)
for i in k[0:len(nums)]:
    if i==k[0] :
       del nums[i]
for x in k[len(nums)+1:0]:
    if x==k(len(nums)):
        del nums[x]
print(nums)

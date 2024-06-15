nums=eval(input())
nums1=nums.count(0)
while nums.count(0)>=1:
    nums.remove(0)
c=[0]*nums1
nums=nums+c
print(nums)




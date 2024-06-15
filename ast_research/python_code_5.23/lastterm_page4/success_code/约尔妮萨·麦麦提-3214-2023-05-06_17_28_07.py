list=eval(input( ))
nums=list
for i in range(len(nums)):
    if nums[i]==0:
        j=i+1
        while j<len(nums):
            if nums[j]!=0:
                nums[i]=nums[j]
                nums[j]=0
                break
            j=j+1

print(nums)

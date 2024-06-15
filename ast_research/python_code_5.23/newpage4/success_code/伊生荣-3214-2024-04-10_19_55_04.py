
def moveZeroes(nums):
    i,j=0,0
    while i<len(nums):
        if nums[i]==0:
            j=i+1
    while j<len (nums):
        if nums[j]!=0:
            temp=nums[i]

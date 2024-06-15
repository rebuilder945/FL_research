def search(self, nums: list[int]) -> int:
     return self.search(nums,0,len(nums)-1)
def search(self,nums,left,right):
    if left == right:
        return nums[left]
    mid = left+ (right-left)//2
    leftmajority = self.search(nums,left,mid)
    rightmajority = self.search(nums,mid+1,right)
    if leftmajority == rightmajority:
        return leftmajority
    leftcount = 0 
    rightcount = 0
    for i in nums[left:right+1]:
        if i == leftmajority:
            leftcount += 1
        else:
            rightcount += 1
    if leftcount > rightcount:
        return leftmajority
    else:
        return rightmajority





nums = eval(input())
y = search(nums)
print(y)



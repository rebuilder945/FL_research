def search(nums):
    nums2=[]
    for x in nums:
        cnt=nums.count(x)
        nums2.append(cnt)
        if cnt>(len(nums)/2):
            return x
    if max(nums2)<=(len(nums)/2):
        return False





nums = eval(input())
y = search(nums)
print(y)



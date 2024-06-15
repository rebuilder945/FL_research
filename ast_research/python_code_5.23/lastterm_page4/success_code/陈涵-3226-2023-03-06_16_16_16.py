def search(nums):
    nums2=[]
    nums3=[]
    for x in nums:
        cnt=nums.count(x)
        nums2.append(cnt)
        if max(nums2)<=(len(nums)/2):
            return False
        else:
            if cnt>(len(nums)/2):
                nums3.append(x)
                return nums3





nums = eval(input())
y = search(nums)
print(y)



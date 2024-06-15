
def search(nums):
    nums2=[]
    for x in nums:
        cnt=nums.count(x)
        nums2.append(cnt)
        if max(nums2)<=(len(nums)/2):
            return False
        else:
            if cnt>(len(nums)/2):
                return x






nums = eval(input())
y = search(nums)
print(y)



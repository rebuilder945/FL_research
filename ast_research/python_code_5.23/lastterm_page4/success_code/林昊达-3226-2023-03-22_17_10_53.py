def search(nums):
    ls=[]
    for i in range(len(nums)):
        ls.append(nums.count(nums[i]))
    x=max(ls)
    if x>len(nums)//2:
        return nums[ls.index(x)]
    else:
        return False





nums = eval(input())
y = search(nums)
print(y)



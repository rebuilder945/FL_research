def search(nums):
    for i in nums :
        n=nums.count(i)
        if n>(len(nums)//2):
            retrun i
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)



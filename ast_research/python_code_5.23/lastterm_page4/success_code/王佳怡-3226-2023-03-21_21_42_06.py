def search(nums):
    for x in range(len(nums)):
        a=nums.count(nums[x])
        if a>len(nums)//2:
            return search
        else:
            print("False")





nums = eval(input())
y = search(nums)
print(y)



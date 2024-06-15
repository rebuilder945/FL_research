def search(nums):
    nums = eval(input())
    n = len(nums)
    ls=[]
    for x in nums:
        n1=nums.count(nums[0])
        n2 = n1 //2
        if n2 >= n:
            print(nums[0])
            if x not in ls:
                ls.extend(nums[0])
                pass
            else:
                nums.romove(nums[0])





nums = eval(input())
y = search(nums)
print(y)



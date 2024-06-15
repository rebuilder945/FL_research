def search(nums):
    n = len(nums)
    ls=[]
    a = False
    for x in nums:
        n1=nums.count(nums[0])
        if n1 //2 >= n:
            a = n1
            if x not in ls:
                ls.append(nums[0])
            else:
                nums.remove(nums[0])
    return a





nums = eval(input())
y = search(nums)
print(y)



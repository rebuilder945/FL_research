def search(nums):
    n=len(nums)
    for x in nums:
        t=nums.count(x)
        if t>=n*0.5:
            return x
        else:
            print(False)






nums = eval(input())
y = search(nums)
print(y)



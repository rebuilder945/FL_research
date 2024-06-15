def search(nums):
    for x in nums:
        l=len(nums)
        l=l/2
        s=nums.count(x)
        if s>l:
            print(s)






nums = eval(input())
y = search(nums)
print(y)



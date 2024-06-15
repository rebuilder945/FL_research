def search(nums):
    n=len(nums)
    for i in nums:
        m=nums.count(i)
        if m>n//2:
            return i
        else :
            print(False)





nums = eval(input())
y = search(nums)
print(y)



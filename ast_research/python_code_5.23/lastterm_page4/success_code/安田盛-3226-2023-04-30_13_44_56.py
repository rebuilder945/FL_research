def search(nums):
    for x in nums:
        n=nums.count(x)
        if n>len(nums) //2:
            return x
        else:
            return False
          





nums = eval(input())
y = search(nums)
print(y)



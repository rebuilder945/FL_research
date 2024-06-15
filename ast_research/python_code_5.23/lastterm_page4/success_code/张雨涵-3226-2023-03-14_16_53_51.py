def search(nums):
    n = len(nums)
    if n > 2:
        for i in nums:
            t = nums.count(i)
            if t >= n//2 :
                return i
            else:
                return "False"
    else:
        return "False"





nums = eval(input())
y = search(nums)
print(y)



def a(nums):
    nums=[str(num) for num in nums]
    nums.sort(reverse=True)
    return ''.join(nums)
b=a(eval(input()))
print(b)


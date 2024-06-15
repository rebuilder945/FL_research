nums = eval(input())
kong = []
inums = []
nums.sort(reverse = True)
n = nums.count(0)
if n == len(nums):
    print(0)
else:
    for i in nums:
        x = str(i)
        kong.append(x)
    print("".join(kong))

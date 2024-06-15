import math
def search(nums):
    nums.sort(reverse = True)
    a = nums[0:-1:math.floor(len(nums)/2)]
    a.pop(0)
    return(a)





nums = eval(input())
y = search(nums)
print(y)



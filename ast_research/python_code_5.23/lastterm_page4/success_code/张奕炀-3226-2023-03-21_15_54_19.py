import math
def search(nums):
    nums.sort(reverse = True)
    a = nums[0:-1:math.floor(len(nums)/2)-1]
    a.pop(0)
    if nums.count(a[0])>len(nums)/2:
        print(a[0])
    else:
        print('False')





nums = eval(input())
y = search(nums)
print(y)



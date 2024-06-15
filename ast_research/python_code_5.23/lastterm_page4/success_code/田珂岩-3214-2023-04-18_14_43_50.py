nums = eval(input())
a = int(nums.count(0))
while 0 in nums:
    nums.remove(0)
ls = nums + [0]*a
print(ls)    


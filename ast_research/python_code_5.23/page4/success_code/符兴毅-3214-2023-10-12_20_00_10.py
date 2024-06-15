nums = eval(input())
a = nums.count(0)
for i in range(nums.count(0)):
    nums.remove(0)
for i in range(a):
    nums.append(0)
print(nums)

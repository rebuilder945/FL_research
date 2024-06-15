nums = eval(input())
zero = nums.conut(0)
while nums.count(0) > 0:
    nums.remove(0)
    zeros = [o]*zero
    nums = nums+zeros
print(nums)


nums = list(map(int, input().strip('[]').split(',')))
average = sum(nums) / len(nums)
print('%.2f' % average)

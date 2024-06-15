nums = eval(input())
average = sum(nums) / len(nums)
if average.is_integer():
    print(int(average))
else:
    print('{:.2f}'.format(average))


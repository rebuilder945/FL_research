nums = eval(input())
nums.sort(reverse=True)
for i in nums:
    if nums[0] == 0:
        print(0)
        break
    else:
        print(i,end='')

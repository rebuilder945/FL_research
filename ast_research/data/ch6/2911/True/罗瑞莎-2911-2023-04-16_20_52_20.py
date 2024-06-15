num = input()
nums = []
for i in range(len(num)):
    nums.append(num[i])
for j in range(len(nums)):
    nums[j] = (int(nums[j])+5)%10
nums.reverse()
for k in range(len(nums)):
    print(nums[k],end='')

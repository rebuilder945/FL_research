nums = eval(input())
aim = []
for i in range(len(nums)):
    if nums.count(nums[i])==1:
        aim.append(nums[i])
aim.sort(reverse=False)
if len(aim)==0:
    print("False")
else:
    for i in range(len(aim)):
        aim[i] = str(aim[i])
    print(','.join(aim))
# print(','.join(aim))

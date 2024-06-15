nums = eval(input())
lst1 = []
for i in range(len(nums)):
    if nums.count(nums[i]) == 1:
        lst1.append(nums[i])
lst1.sort()
if len(lst1) == 0:
    print(False)
else:
    for j in range(len(lst1)):
        print(lst1[j],sep=',')

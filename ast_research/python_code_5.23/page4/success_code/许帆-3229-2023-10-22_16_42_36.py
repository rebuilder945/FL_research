nums = eval(input())
lst1 = []
for i in range(len(nums)):
    if not nums.count(nums[i]) == 1:
        print(False)
        break
    if nums.count(nums[i]) == 1:
        lst1.append(nums[i])
        lst1.sort()
        for j in range(len(lst1)):
            print(lst1[j],sep=',')

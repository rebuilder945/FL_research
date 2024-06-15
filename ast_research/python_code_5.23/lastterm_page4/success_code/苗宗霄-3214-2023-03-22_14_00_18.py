def moveZeroes(nums):
    i,j = 0, 0
    while i < len(nums):
        if nums[i] == 0:
            j = j + 1
            while j < len(nums):
                if nums[j] !=0:
                    temp = nums[j]
                    nums[j] = nums[j]
                    nums[j] = temp
                    break
                j += 1
            if j >= len(nums):
                break
        i += 1
    print(nums)



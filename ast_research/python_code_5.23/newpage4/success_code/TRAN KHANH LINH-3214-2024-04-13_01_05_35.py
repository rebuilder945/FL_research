def move_zeros(nums):
    count_zeros = nums.count(0)
    nums = [num for num in nums if num != 0]
    nums.extend([0] * count_zeros)
    return nums

input_str = input()
nums = [int(num) for num in input_str.strip("[]").split(",")]
result = move_zeros(nums)
print(result)


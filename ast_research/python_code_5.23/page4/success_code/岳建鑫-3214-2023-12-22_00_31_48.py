def move_zeros(nums):
    zeros = []
    non_zeros = []
    
    for num in nums:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    return non_zeros + zeros


input_str = input()
# 去除方括号，并按逗号分隔字符串，得到整数列表
nums = [int(num) for num in input_str.strip('[]').split(',')]

result = move_zeros(nums)
print(result)


def move_zeros(nums):
    zeros = [num for num in nums if num == 0]
    non_zeros = [num for num in nums if num != 0]
    return non_zeros + zeros
# 示例输入
input_list = [1, 0, 2, 0, 3, 0]
# 调用函数并打印输出
print(move_zeros(input_list))

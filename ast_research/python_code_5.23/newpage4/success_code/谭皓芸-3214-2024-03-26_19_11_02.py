def move_zeros_to_end(lst):
    return sorted(lst, key=lambda x: x == 0)
nums = [int(x) for x in input().split(',')]
result = move_zeros_to_end(nums)
print(result)

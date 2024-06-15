def construct_max_number():
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    max_num = ''
    for num in nums:
        max_num += str(num)
    return int(max_num)

print(construct_max_number())

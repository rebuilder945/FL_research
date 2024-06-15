def create_max_number(nums):
    sorted_nums = sorted(nums,reverse=True)
    max_number_str = ''.jion(map(str, sorted_nums))
    max_number = int(max_number_str)
    return max_number
nums = [0,1,2,3,2]
print(create_max_number(nums))

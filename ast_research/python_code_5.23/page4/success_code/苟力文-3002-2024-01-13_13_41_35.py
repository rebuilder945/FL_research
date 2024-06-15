def average(input_str):
    nums = [int(x) for x in input_str.strip('[]').split(',')]
    total = sum(nums)
    avg = total / len(nums)
    if avg.is_integer():
        return int(avg)
    else:
        return round(avg, 2)

input_str = input()
print(average(input_str))


def find_unique_elements(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        unique_elements = [num for num, freq in count.items() if freq == 1]
    
    if unique_elements:
        return ','.join(map(str, sorted(unique_elements)))
    else:
        return "False"
input_str = input()
num_list = [int(x) for x in input_str.strip('[]').split(',')]
result = find_unique_elements(num_list)
print(result)


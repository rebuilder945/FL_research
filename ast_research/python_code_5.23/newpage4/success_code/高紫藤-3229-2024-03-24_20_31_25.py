
nums = input().strip('[]').split(',')
count_dict = {}
result = []
for num in nums:
    count_dict[num] = count_dict.get(num, 0) + 1
for num, count in count_dict.items():
    if count == 1:
        result.append(int(num))
if not result:
    print(False)
else:
    result.sort()
    result_str = ','.join(str(num) for num in result)
    print(result_str)

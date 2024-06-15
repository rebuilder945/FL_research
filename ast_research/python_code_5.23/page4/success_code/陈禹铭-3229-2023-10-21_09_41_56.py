nums = eval(input())
counts = {}
for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
unique_nums = [num for num, count in counts.items() if count == 1]
if unique_nums:
    unique_nums.sort()
    result = ','.join(map(str, unique_nums))
    print(result)
else:
    print("False")


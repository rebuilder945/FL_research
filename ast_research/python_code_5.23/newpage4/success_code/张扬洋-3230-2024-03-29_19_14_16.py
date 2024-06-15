def largest_number(nums):
    def compare(x,y):
        return int(y + x) - int(x + y)
    sorted_nums = sorted(nums,key=lambda x: str(x),reverse=True)
    sorted_nums.sort(key=cmp_to_key(compare))
    result = ''.join(map(str,sorted_nums))
    while result.startswith('0') and len(result) > 1:
        result = result[1:]
    return result

nums = list(map(int,input().split()))
print(largest_number(nums))


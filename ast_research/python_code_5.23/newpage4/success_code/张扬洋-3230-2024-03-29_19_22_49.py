def largest_number(nums):
    def compare(x,y):
        if x == 0:
            return 1 if y != 0 else 0
        if y == 0:
            return -1 if x != 0 else 0
        return int(str(y) +str(x)) - int(str(x) + str(y)) 
    sorted_nums = sorted(nums,key=lambda x: str(x),reverse=True)
    sorted_nums.sort(key=cmp_to_key(compare))
    result = ''.join(map(str,sorted_nums))
    if result == '0' * len(nums):
        return '0'
    return result.latrip('0')
    
nums = list(map(int,input().split()))
print(largest_number(nums))


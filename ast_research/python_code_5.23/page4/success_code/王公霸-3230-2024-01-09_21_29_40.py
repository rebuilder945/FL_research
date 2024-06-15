def max_number(nums):
        nums.sort(reverse=True)   
        result = int(''.join(map(str, nums)))   
        return result
nums = eval(input())
print(max_number(nums))


    
    

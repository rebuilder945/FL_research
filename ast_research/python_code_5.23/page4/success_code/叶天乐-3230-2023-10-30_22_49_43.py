def numbers(nums):
    nums = list(map(str,nums))
    sort(key = lambda x:x*10,reverse=True)
    numbers = ''.join(nums)
    return'0' if numbers[0]=='0' else numbers

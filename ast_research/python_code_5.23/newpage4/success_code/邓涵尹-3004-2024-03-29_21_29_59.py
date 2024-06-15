#def ps(nums):
#    c={}
#    for num in nums:
#        for b in range(1,10):
#            if num % b == 0:
#                del nums[num]
#            else:
#                nums.append(num)
#
#nums = eval(input())
#print(ps(nums))



def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

input_list = list(map(int, input("请输入一个自然数列表： ").split(',')))
output_list = [num for num in input_list if is_prime(num)]
print(output_list)

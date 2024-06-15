nums = input().split()  
nums = [int(num) for num in nums] 
avg = sum(nums) / len(nums)  
if avg % 1 == 0:  
    print(int(avg)) 
else:
    print('%.2f' % avg)  

def max_(nums):  
    nums.sort()  
    num = ''  
    for i in range(len(nums)):  
        if i == 0 or nums[i] != nums[i-1]:  
            num += str(nums[i])  
    return int(num)  
  
s = input()  
a = [int(num) for num in s.split()]    
print(int(max_(a)))

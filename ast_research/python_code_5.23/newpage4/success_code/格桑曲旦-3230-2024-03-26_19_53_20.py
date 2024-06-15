def largest_number(nums):
    nums=[str(num) for num in nums]
    def compare(x,y):
        return int(y+x)-int(x+y)
    nums.sort(key=compare)
    largest_num=int(''.join(nums))
    return largest_num
nums=[1,2,3,4]
result=largest_number(nums)
print(result)




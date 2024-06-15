def build_max_number(nums):
    nums.sort(reverse=True)
    result=[nums[0]]
    for i in range(1,len(nums)):
        j=0
        while j <len(result) and nums[i]>result[j]:
            j+=1
        if j==len(result):
            result.append(nums[i])
        else:
            result.insert(j,nums[i])
    
    result 
    int(''.join(str(x) for x in result))
a=eval(input())
b=build_max_number(a)
print(b)

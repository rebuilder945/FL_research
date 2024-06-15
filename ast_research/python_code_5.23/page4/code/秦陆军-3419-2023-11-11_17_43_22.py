def  calDegrees(nums):
    fre_cout = {}
    max_fre = 0
    for num in nums:
       if num in fre_count:
         fre_count[num]+=1
       else:
         fre_count[num]=1
       max_fre = max(fre_count[num],max_fre)
     return max_fre


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


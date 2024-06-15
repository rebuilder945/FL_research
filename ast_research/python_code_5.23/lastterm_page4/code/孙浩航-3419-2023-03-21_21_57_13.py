def calDegrees(nums):
&#160; &#160; ls2=[]
&#160; &#160;   for x in nums:
&#160; &#160; &#160; &#160; wi=nums.count(x)
&#160; &#160; &#160; &#160; ls2.append(wi)
&#160; &#160; return max(ls2)
 
    
    
   


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


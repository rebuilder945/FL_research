def alDegrees(self, nums: List[int]) -> int:
       #用来保存出现的次数，第一次出现的位置，最后一次出现的位置
    mp = dict()
    for i,num in enumerate(nums):
        if num in mp:
            mp[num][0]+=1
            mp[num][2] =i
        else:
            mp[num]=[1,i,i]
        
    max_num=0
    min_len=0
        #对字典进行检索
    for count,left,right in mp.values():
            #如果当前的数字的频率比max_num高
        if max_num<count:
           max_num = count
           min_len = right - left + 1
            #如果当前数字的频率和max_num一样，这时候就比较一下最短长度看谁短
        elif max_num==count:
            if min_len>(right-left+1):
                min_len = right-left+1
    return min_len


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


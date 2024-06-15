# 2023-2024（2）基础题库练习：第4章
# 第一题
# lst=eval(input())
# lst.sort(reverse=True)
# sum=''
# for i in range(len(lst)):
#     sum+=str(lst[i])
# print(int(sum))

# 第二题
nums=eval(input())
def find_once(nums):
    count={}
    for num in nums:
        if num in nums:
            count[num]+=1
        else:
            count[num]=1
    once_nums=[num for num,freq in count.items() if freq==1]
    if once_nums:
        a=once_nums.sort()
        print('a')
    else:
        print('False')        
        

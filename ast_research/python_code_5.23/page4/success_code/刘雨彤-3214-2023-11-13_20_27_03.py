nums=eval(input())
for num in nums:
    jishu=0
    if num==0:
        nums.remove(num)
        jishu+=1
    add=[0]*jishu
    res=nums+add
    print(res)

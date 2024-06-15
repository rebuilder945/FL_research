def calDegrees(num):
    dic={}
    for i in num:
        if i not in dic:
           dic[1]=1
        else:
            dic[i]+=1
    return max(dic.values())



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


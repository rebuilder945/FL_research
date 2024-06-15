dic={}
def calDegrees(a) :
    for i in a:
        if i in dic:
            dic[i]+=1
        else i not in dic:
            dic[i]=1
     b=max(dic.values())
    return b

    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


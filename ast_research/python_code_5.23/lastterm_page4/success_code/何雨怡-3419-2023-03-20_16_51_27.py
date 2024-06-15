def calDegrees(lst):
    fre=[]
    for i in lst:
        counter=lst.count(i)
        fre.append(counter)
    number=max(fre)
    return number


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


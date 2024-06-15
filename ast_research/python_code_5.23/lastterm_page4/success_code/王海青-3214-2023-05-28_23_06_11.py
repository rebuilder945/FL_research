def f1(nums):
    b=[]
    c=[]    
    for i in nums:
        if i % 2 == 0:
            c.append(i)
        else:
            pass
            b.append(i)
    d = b + c
    return d
nums = eval(input())
print(f1(nums)) #调用自定义函数

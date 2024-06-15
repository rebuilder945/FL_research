 def calDegrees(n):
    c = 0
    for i in n:
        if n.count(i) > c:
            c =n.count(i)
    return  c 



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


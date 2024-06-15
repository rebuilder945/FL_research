def calDegrees(Ist=[]):
     temp=set(Ist)
     d=0
     for i in temp :
         time=Ist.count(i)
         if time > times:
            d = time
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


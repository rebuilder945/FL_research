def calDegrees(Ist=[]):
     temp=set(Ist)
     times=0
     for i in temp :
         time=Ist.count(i)
         if time > times:
            times = time
     print(times)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


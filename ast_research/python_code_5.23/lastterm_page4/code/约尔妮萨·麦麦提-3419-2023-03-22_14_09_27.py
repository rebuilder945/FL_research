def search(y):
       for x in y :
            if(y.count(x)>(len(y)//2))
                 return x
       return Flase;


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


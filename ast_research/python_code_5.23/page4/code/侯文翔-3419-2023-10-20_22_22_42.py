def calDegrees(y):
       z=0
        ls=[]
        for x in y:
              if y.count(x)>z:
                   z=y.count(x)
                    ls.append(z)
         print(max(ls))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)


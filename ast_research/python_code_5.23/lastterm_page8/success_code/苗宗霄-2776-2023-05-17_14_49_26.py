def  myFun(a,b):
           if not a.isdigit() or not b.isdigit():  # 判断 a,b 是否都是数字
               return "error"
           s = 0                                   # 记录乘积和
           for x, y in zip(a, b):                  # 按位迭代
               s += int(x) * int(y)
           return s                                # 返回乘积和


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


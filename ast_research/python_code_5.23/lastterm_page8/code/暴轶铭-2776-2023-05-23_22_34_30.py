def  myFun(a,b):
           sum = 0
           if a.isdigit() and b.isdigit(): #判断 a,b 是否都为正整数
               n1 = len(a) # a 的位数
               n2 = len(b) # b 的位数
               n = min(n1, n2) # 取 a,b 中较小的位数 n
               for i in range(n):
                   sum += int(a[n1-i-1])*int(b[n2-i-1]) # 累加每一位的乘积
               return sum
           else:
               return "error"
       if a.isdigit() and b.isdigit(): #判断 a, b 是否都为正整数
       n1 = len(a) # a 的位数
       n2 = len(b) # b 的位数
       n = min(n1, n2) # 取 a, b 中较小的位数 n在范围内(N)：
       sum += int(a[n1-i-1])*int(b[n2-i-1]) # 累加每一位的乘积回报和其他：返回“错误”

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


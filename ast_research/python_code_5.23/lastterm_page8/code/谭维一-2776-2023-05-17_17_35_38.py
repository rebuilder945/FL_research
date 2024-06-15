def  myFun(a,b):
       len_a, len_b = len(a), len(b)
       n = min(len_a, len_b)
       sum_product = 0
       for i in range(n:):
           sum_product += int(a[i]) * int(b[i])

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


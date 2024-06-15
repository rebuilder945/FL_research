def  myFun(a,b):
       long = max(len(n), len(m))
       sum = 0
       while len(n) < long:
           n = '0' + n
       while len(m) < long:
           m = '0' + m
       for i in range(long):
           sum += int(n[i]) * int(m[i])


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


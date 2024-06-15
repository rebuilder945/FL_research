def  myFun(a,b):
           s = 0
           if len(a) > len(b):
               x = len(b)
           else:
               x = len(a)
           for i in range(-1,-x-1,-1):
               s += int(a[i]) * int(b[i])
           return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


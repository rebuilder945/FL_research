def  myFun(a,b):
           c = len(a)
           d = len(b)
           e = max(c,d)
           a = "0"*(e-c)+a
           b = "0"*(e-d)+b
           s = 0
           for i in range(e):
               x,y = int(a[i]),int(b[i])
               s = s+x*y
           return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


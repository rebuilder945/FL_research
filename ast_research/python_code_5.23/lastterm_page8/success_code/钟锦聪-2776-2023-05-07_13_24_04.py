def  myFun(a,b):
           c = str(a)
           d = str(b)
           e = min(len(str(a)),len(str(b)))
           f = 0
           for i in range(e):
               f += int(c[-1-i])*int(d[-1-i])
           return f

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


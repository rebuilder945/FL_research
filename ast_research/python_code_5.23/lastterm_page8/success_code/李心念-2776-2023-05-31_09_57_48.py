def  myFun(a,b):
       b = 0
       if eval(a) <= eval(b):
           for x in range(len(a)):
               b += a[::-1][x] * b[::-1][x]
       else:
           return myFun(b,a)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


def  myFun(a,b):
           n = 0
           c = str(a)
           d = str(b)
           if b > a:
               for x in range(len(a)):
                   n += int(c[-x-1]) * int(d[-x-1])
           else:
               for x in range(len(b)):
                   n += int(c[-x-1]) * int(d[-x-1])

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


def  myFun(a,b):
           ls1 = list(a)
           ls2 = list(b)
           length = 0
           total = 0
           if len(ls1) > len(ls2):
               length = len(ls2)
           else:
               length = len(ls1)
       
           for i in range(1, length + 1):
               total += int(ls1[-i]) * int(ls2[-i])
           
           return total

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")

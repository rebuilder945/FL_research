def  myFun(a,b):
           if not (isinstance(a, str) and isinstance(b, str)):
               return "error"
       
           result = 0
           for i, d1 in enumerate(a):
               if not d1.isdigit():
                   return "error"
               for j, d2 in enumerate(b):
                   if not d2.isdigit():
                       return "error"
                   if i == j:
                       result += int(d1) * int(d2)
       
           return result

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


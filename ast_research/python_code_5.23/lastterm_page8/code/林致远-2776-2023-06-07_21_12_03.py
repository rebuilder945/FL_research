def  myFun(a,b):
         if b > a:
           return count(str(a),str(b))
         else:
           return count(str(b),str(a))
       def count(l,s):
         n = 0
         for x in range(len(s)):
           n += int(l[-x-1]) * int(s[-x-1])
         return n

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


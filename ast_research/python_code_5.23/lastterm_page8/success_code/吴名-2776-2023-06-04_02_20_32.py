def  myFun(a,b):
       result = 0
       if len(a)==len(b):
           for i in range(len(a)):
               result += int(a[i]) * int(b[i])
       if len(a)>=len(b):
           for i in range(len(b)):
               result += int(a[len(b)-i]) * int(b[len(b)-i])
       if len(a)<=len(b):
           for i in range(len(a)):
               result += int(a[len(a)-i]) * int(b[len()-i])
       return result

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


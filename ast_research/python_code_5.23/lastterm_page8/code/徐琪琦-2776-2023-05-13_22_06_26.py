def  myFun(a,b):
       if a <0 or b <0 or type(a)!= int or type(b)!= int:
           return "error"
       else:
           s = 0
           for i in str(a):
               for j in str(b):
                s += int(i)*int(j)
            return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


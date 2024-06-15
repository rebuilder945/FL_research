def  myFun(a,b):
       if int(a) <0 or int(b) <0 or type(eval(a))!= int or type(eval(b))!= int:
           return "error"
       else:
           s = 0
           for i in str(a)[::-1]:
               for j in str(b)[::-1]:
                s += int(i)*int(j)
           return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


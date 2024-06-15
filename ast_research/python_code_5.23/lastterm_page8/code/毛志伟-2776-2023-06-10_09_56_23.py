def  myFun(a,b):
       c = 0
       for i in range(min(len(a),len(b))):
           c+= (eval(a[::-1][i])*eval(b[::-1][i])
       return c    

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


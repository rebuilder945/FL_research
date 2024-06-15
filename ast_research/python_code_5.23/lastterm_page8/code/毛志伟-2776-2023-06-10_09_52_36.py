def  myFun(a,b):
       c = 0
       for i in min(len(a),len(b)):
           c+= (int(a[::-1])*int(b[::-1])    

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


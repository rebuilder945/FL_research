def  myFun(a,b):
       long=min(len(a),len(b))
       sum=0
       for i in range(long):
         sum=int(a[i])*int(b[i-1])
       return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


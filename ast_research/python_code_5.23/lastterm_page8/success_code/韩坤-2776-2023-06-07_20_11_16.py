def  myFun(a,b):
       a=str(a)
       b=str(b)
       s=0
       for i in range(-1,-min(len(a),len(b))-1,-1):
           s=s+int(a[i])*int(b[i])
       return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


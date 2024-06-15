def  myFun(a,b):
       c=min(len(a),len(b))
       n=0
       for i in range(-1,-c-1,-1):
           n=n+int(b[i])*int(a[i])
       return n  

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


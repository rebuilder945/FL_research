def  myFun(a,b):
       s=0
           mi=min(len(a),len(b))
           for i in range(mi):
               s+=int(a[-(i+1)])*int(b[-(i+1)])
           return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


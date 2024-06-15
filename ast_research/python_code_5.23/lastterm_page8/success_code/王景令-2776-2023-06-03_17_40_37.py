def  myFun(a,b):
       def myFun(a,b):
           d = max(len(a),len(b))
           a,b = a.zfill(d),b.zfill(d)
           c = 0
           for i in range(d):
               c += int(a[i])*int(b[i])
           return c

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


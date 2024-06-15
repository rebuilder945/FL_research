def  myFun(a,b):
       a = list(a)
       b = list(b)
       w=min(len(a),len(b))
       e=0
       for i in range(w):
           e+=int(a.pop())*int(b.pop())
       return e


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


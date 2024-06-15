def  myFun(a,b):
       a,b=eval(a),eval(b)
       if type(a)!=type(1) or type(b)!=type(1):
           return "error"
       res=0
       while a and b:
           res+=(a%10)*(b%10)
           a/=10
           b/=10
       return res

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


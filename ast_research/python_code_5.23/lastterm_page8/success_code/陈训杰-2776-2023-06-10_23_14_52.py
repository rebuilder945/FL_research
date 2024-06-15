def  myFun(a,b):
       if eval(a)<=0 or eval(b)<=0:
           print("errot")
       else:
           sum=0
           for i in range(1,min([len(a),len(b)])+1):
               sum+=eval(a[-i])*eval(b[-i])
       return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


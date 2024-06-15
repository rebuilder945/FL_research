def  myFun(a,b):
       mysum=0
       for x in range(min(len(a),len(b))):
           musum=mysum+eval(a[::-1][x])*eval(b[::-1][x])
       return mysum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


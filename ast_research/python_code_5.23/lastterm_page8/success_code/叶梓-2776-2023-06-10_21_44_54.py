def  myFun(a,b):
       l=min([len(a),len(b)])
       sum=0
       for x in range(1,l+1):
           sum+=eval(a[-x])*eval(b[-x])
       return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


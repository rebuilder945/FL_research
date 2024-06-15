def  myFun(a,b):
       result=0
       for i in range(0,min(len(a),len(b))):
           result += int(a[-i-i])*int(b[-i-1])
       return result

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


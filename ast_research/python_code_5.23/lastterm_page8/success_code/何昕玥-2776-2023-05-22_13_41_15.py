def  myFun(a,b):
       if a<0 or b<0:
          return error
       else:
          sum=0
          for i in range(max(len(a),len(b))):
                sum+=((a%10)*(b%10))
                a=a//10
                b=b//10
       return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


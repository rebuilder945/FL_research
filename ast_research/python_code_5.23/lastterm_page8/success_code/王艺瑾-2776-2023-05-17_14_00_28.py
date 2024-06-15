def  myFun(a,b):
       c=min([len(a),len(b)])
       a=int(a)
       b=int(b)
       sum=0
       for i in range(1,c+1):
           d=10*i
           sum+=(a%d)*(b%d)
           a//10
           b//10
       return sum
           
       
           

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


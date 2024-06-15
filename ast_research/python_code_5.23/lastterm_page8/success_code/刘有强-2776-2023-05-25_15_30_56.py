def  myFun(a,b):
                     a = int(a)
                     b = int(b)
                     sum=0
                     while True:
                            if a==0 and b==0:
                                   break
                            sum=sum+((a%10)*(b%10))
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


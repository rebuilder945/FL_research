def  myFun(a,b):
       n=max[a,b]
       as=[]
       bs=[]
       for x in range(n):
           as.append(a%10)
           bs.append(b%10)
           a=a//10
           b=b//10
       sumnumber=0
       for i in range(len(as)):
           sumnumber+=as[i]+bs[i]
       return sumnumber

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


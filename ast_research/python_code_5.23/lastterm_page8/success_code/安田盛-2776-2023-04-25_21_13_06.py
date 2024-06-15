def  myFun(a,b):
       a=a[len(a)-len(b):]
       x=0
       for i in range(len(b),0,-1):
           c=int(a[i-1])*int(b[i-1])
           x+=c
       return(x)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


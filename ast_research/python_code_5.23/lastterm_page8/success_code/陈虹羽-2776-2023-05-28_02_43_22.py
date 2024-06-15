def  myFun(a,b):
            a1=len(a)
            b1=len(b)
            d=min(a1,b1)
            c=0
            for  i in range(1,d+1):     
               c+=int(a[-i])*int(b[-i])         
            return c 


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


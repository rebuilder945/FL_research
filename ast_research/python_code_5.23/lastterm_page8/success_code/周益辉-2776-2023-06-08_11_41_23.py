def  myFun(a,b):
           a=eval(a)
           b=eval(b)
           if type(a)==float or type(b)==float:
               print('error')
       
           changdu=0
           if len(a)>=len(b):
               changdu=len(a)
           else:
               changdu=len(b)
           sum=0
           ji=1
           a=str(a)
           b=str(b)
           for i in range(1,changdu+1):
               ji=int(a[-i])*int(b[-i])
               sum+=ji
           
           return sum

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


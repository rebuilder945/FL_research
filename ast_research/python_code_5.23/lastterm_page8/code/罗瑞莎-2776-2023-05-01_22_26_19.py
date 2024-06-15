def  myFun(a,b):
       lsta = []
       lstb = []
       n = 0
       if a>0 and b>0 and a%1==0 and b%1==0:
           for i in range(len(a)):
               lsta.append(a[i])
           for j in range(len(b)):
               lstb.append(b[i])
           if len(a) > len(b):
               for k in range(1,len(b)+1):
                   n += int(lsta[-i])*int(lstb[-i])
               return n
           if len(a) < len(b):
               for k in range(1,len(a)+1):
                   n += int(lsta[-i])*int(lstb[-i])
               return n
       else:
       print("error")
           

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


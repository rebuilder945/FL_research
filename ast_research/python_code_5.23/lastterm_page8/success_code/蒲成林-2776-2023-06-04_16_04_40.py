def  myFun(a,b):
               sd=[]
               a2=str(a)[::-1]
               b2=str(b)[::-1]
               c=min(len(a2),len(b2))
               for i in range(c):
                       d=int(a2[i])*int(b2[i])
                       sd.append(d)
               return sum(sd)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


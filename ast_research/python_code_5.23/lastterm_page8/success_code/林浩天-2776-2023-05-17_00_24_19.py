def  myFun(a,b):
       a1=list(a)
       b1=list(b)
       end=0
       if len(a1)>=len(b1):
           for i in range(1,len(b1)+1):
               end+=(int(b1[-i]))*(int(a1[-i]))
       else:
           for i in range(1,len(a1)+1):
               end+=(int(b1[-i]))*(int(a1[-i]))
       return end        

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


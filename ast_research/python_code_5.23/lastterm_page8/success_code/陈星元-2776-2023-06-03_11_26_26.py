def  myFun(a,b):
           a=eval(a)
           b=eval(b)
           sum=0
           if isinstance(a,int)and isinstance(b,int):
               ls1=[]
               ls2=[]
               for i in str(a):
                   ls1.append(i)
               for i in str(b):
                   ls2.append(i)
               ls1.reverse()
               ls2.reverse()
               for i in range(min(len(ls1),len(ls2))):
                   sum+=int(ls1[i])*int(ls2[i])
               return sum
           else:
               return "error"

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


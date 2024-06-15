def  myFun(a,b):
           if type(eval(a))==int and type(eval(b))==int and eval(a)>0 and eval(b)>0:
               stra=str(a)
               strb=str(b)
               sum=0
               if len(stra)==len(strb):
                   for i in range(len(stra)):
                       cheng=int(stra[i])*int(strb[i])
                       sum+=cheng
               elif len(stra)>len(strb):
                   restra=stra[::-1]
                   restrb=strb[::-1]
                   for i in range(len(strb)):
                       cheng=int(restrb[i])*int(restra[i])
                       sum+=cheng
               else:
                   restrb=strb[::-1]
                   restra=stra[::-1]
                   for i in range(len(stra)):
                       cheng=int(stra[i])*int(restrb[i])
                       sum+=cheng
               return sum
           else:
               return 'error'

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


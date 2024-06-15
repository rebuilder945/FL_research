def  myFun(a,b):
           sums=0
           if len(a)>=len(b):
               for i in range(-1,-len(b)-1,-1):
                   sums+=int(a[i])*int(b[i])
           elif len(b)>len(a):
               for i in range(-1,-len(a)-1,-1):
                   sums+=int(a[i])*int(b[i])   
           return sums        
           elif len(b)>len(a):
               for i in range(-len(a),0):
                   c=int(a[i])
                   d=int(b[i])
                   sum2=c*d
                   sum1 += sum2
               return sum1 

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


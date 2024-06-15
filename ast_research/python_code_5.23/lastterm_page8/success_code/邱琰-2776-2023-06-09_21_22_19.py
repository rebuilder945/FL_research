def  myFun(a,b):
       s=0
       while int(a)==0 and int(b)==0:
           c=int(a)%10
           d=int(b)%10
           a=str(int(a)//10)
           b=str(int(b)//10)
           s+=c*d
           return s
           

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


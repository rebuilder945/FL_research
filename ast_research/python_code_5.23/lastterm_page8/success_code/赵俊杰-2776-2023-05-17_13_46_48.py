def  myFun(a,b):
       m=len(a)
       n=len(b)
       s=0
       while m>0 and n>0:
          s=int(a[m-1])*int(b[n-1])+s
          m-=1
          n-=1
       return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


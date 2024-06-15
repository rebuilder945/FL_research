def  myFun(a,b):
           a=a[::-1]
           b=b[::-1]
           i=j=0
           s=0
           while i<len(a) and j<len(b):
               s=s+eval(a[i])*eval(b[j])
               i+=1
               j+=1
           return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


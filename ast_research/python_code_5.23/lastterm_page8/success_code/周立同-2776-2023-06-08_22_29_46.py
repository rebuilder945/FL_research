def  myFun(a,b):
           jishu=0
           jishu2=0
           if int(b)>int(a):
               for i in range(0,len(a)):
                   jishu2=jishu2+1
               lst=[-x for x in range(1,jishu2+1)]
               for i in lst:
                   m=int(a[i])
                   n=int(b[i])
                   jishu=jishu+m*n
               return jishu
           else:
               for i in range(0,len(b)):
                   jishu2=jishu2+1
               lst=[-x for x in range(1,jishu2+1)]
               for i in lst:
                   m=int(a[i])
                   n=int(b[i])
                   jishu=jishu+m*n
               return jishu

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


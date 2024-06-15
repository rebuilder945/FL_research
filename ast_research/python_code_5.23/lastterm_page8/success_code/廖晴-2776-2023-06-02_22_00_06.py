def  myFun(a,b):
               if int(a)<=0 or int(b)<=0:
                       print('error')
               else:
                       A=max(a,b)
                       B=min(a,b)
                       A=list(str(A))
                       B=list(str(B))
                       A.reverse()
                       B.reverse()
                       he=0
                       
                       for i in range(len(B)):
                               he=he+int(A[i])*int(B[i])
                       return he

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


def  myFun(a,b):
           sa=str(a)
           sb=str(b)
           result=0
           if len(sa)==len(sb):
              for i in range(0,len(sa)):
                 result=int(sa[i])*int(sb[i])+result 
           if len(sa)>len(sb):
               m=-1
               for i in range(0,len(sb)):
                   result=int(sa[m])*int(sb[m])+result
                   m-=1
           if len(sb)>len(sa):
               m=-1
               for i in range(0,len(sa)):
                   result=int(sb[m])*int(sa[m])+result
                   m-=1
           return result

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


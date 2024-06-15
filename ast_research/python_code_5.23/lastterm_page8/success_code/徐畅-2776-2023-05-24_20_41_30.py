def  myFun(a,b):
               c=0
               lst1=list(a)
               lst2=list(b)
               lst1.reverse()
               lst2.reverse()
               for x in range(min(len(lst1),len(lst2))):
                       c=c+eval(lst1[x])*eval(lst2[x])
               return c

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


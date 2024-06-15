def  myFun(a,b):
       if eval(a)%1!=0 or eval(b)%1!=0:
            return "error"
       else:
            list1=list(a)
            list2=list(b)
            a=len(list1)
            b=len(list1)
            sum=0
            while a==b:
                     if a>b:
                          del list1[0]
                          a-=1
                     elif b>a:
                          del list2[0]
                          b-=1
                     else:
                          for i in range(0,len(list1)):
                                sum+=int(list1[i])*int(list2[i])
                          break
            return sum
                                 

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


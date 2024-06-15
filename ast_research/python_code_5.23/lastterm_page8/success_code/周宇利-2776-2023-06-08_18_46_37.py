def  myFun(a,b):
       if eval(a)%1!=0 or eval(b)%1!=0:
            return "error"
       else:
            list1=list(a)
            list2=list(b)
            while len(list1)==len(list2):
                     if len(list1)>len(list2):
                          del list1[0]
                     elif len(list1)<len(list2):
                          del list2[0]
                     else:
                          for i in range(0,len(list1)):
                                return list1[i]*list2[i]
                                 

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


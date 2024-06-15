def  myFun(a,b):
       if a%1!=0 or b%1!=0:
            return "error"
       else:
            list1=list(a)
            list2=list(b)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


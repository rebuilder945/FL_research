def  myFun(a,b):
       lsta=list(a)
       lstb=list(b)
       while True:
           if len(lsta)>len(lstb):
               lstb.insert(0,0)
           elif len(lsta)<len(lstb):
               lsta.insert(0,0)
           else:
               break
       result=0
       for x in range(0,len(lsta)):
           result=result+int(lsta[x])*int(lstb[x])
       return(result)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


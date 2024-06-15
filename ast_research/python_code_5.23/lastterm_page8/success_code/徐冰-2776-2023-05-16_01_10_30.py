def  myFun(a,b):
       a=str(a)
       ls1=list(a)
       ls2=list(str(b))
       ls11=[int(x) for x in ls1]
       ls22=[int(x) for x in ls2]
       ls3=[]
       if len(ls11)==len(ls22):
           ls11=ls11
       elif len(ls11)>len(ls22):
           ls22=[0]*(len(ls11)-len(ls22))+ls22
       else:
           ls11=[0]*(len(ls22)-len(ls11))+ls11
       for i in range(len(ls11)):
           ls3.append(ls11[i]*ls22[i])
       return sum(ls3)

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


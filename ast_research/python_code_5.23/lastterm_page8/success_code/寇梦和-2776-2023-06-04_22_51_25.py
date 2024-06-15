def  myFun(a,b):
                     lst1=list(map(int,list(a)))
                     lst2=list(map(int,list(b)))
                     lst=list(zip(lst1[::-1],lst2[::-1]))
                     sum=0
                     for x,y in lst:
                         sum+=x*y
                     return sum


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


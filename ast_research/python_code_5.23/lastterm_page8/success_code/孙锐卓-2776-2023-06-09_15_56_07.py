def  myFun(a,b):
       m = [x for x in str(a)]
       n = [x for x in str(b)]
       c = min(len(m), len(n))
       s = 0
       for i in range(c):
           s += int(m[i]) * int(n[i])
       return 


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


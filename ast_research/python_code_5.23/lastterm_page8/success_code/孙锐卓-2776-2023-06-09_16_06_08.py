def  myFun(a,b):
       m = [int(x) for x in str(a)]
       n = [int(x) for x in str(b)]
       c = min(len(m), len(n))
       s = 0
       for i in range(-c,0):
           s += m[i] * n[i]
       return s


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


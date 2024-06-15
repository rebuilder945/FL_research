def  myFun(a,b):
           a, b = float(a), float(b)
           if int(a)==a and int(b)==b and a>0 and b>0:
               a, b = int(a), int(b)
               s = 0
               while True:
                   if a == 0 and b == 0:
                       break
                   s = s + ((a%10)*(b%10))   # 思路：将a,b从最低位开始除余运算后相乘，直到a和b的首位都是0
                   a = a//10
                   b = b//10
               return s
           else:
               return "error"

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


def  myFun(a,b):
           if not a.isdigit() or not b.isdigit():
               return "error"
       
           result = 0
           for digit_a, digit_b in zip(a, b):
               result += int(digit_a) * int(digit_b)
       
           return result


num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


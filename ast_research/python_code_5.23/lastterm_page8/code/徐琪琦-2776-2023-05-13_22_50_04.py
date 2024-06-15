def  myFun(a,b):
       if int(a) <0 or int(b) <0 or type(eval(a))!= int or type(eval(b))!= int:
               return "error"
           else:
               s = 0
               a = [x for x in str(a)]
               b = [x for x in str(b)]
               len1 = len(a)
               len2 = len(b)
               a.reverse()
               b.reverse()
               for i in range(min(len1,len2)):               #可以这样表示欸 
                   s += a[i]*b[i]
               return s

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


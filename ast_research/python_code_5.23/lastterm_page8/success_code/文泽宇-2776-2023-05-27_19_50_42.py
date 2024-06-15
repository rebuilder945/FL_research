def  myFun(a,b):
           if float(a)==int(a) and float(b)==int(b):
               a1 = str(a)
               b1 = str(b)
               lst1 = [int(n) for n in a1]
               lst2 = [int(n) for n in b1]
       
               if len(lst1) == len(lst2):
                   kao = []
                   for i in range(len(lst1)):
                       cao = lst1[i] * lst2[i]
                       kao.append(cao)
                   return sum(kao)
               elif len(lst1) > len(lst2):
                   kao = []
                   for i in range((-1) * len(lst2), 0):
                       cao = lst1[i] * lst2[i]
                       kao.append(cao)
                   return sum(kao)
               elif len(lst2) > len(lst1):
                   kao = []
                   for i in range((-1) * len(lst1), 0):
                       cao = lst1[i] * lst2[i]
                       kao.append(cao)
                   return sum(kao)
           else:
               return "error"

num=input().split()
a=num[0]
b=num[1]
if a.isdigit() and b.isdigit(): #判断a,b是否都是数字
       print(myFun(a,b))  #调用自定义函数
else:
       print("error")


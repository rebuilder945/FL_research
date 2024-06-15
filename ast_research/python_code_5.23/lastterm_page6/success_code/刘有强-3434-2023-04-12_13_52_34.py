# 如何快速地注释语句以及取消注释
# 快捷键：Ctrl+'/'

# print("Hello World") 
# 函数 参数

# 变量 变量的命名规则p8
# 我买了 3 斤苹果，每斤 3.6 元，一共花了 10.8 元，妈妈给我20元，还剩下 9.2 元。

# n = 3
# fPrice = 3.6
# fMount = n * fPrice
# fMoney = 20
# fMoney = fMoney - fMount
# sText1 = "我买了"

# print(sText1,n,"斤苹果，每斤",fPrice,"元，一共花了",
#       fMount,"元，妈妈给我20元，还剩下",fMoney,"元。")

# 占位符  %s 字符串
#        %d 整数
#        %.2f 精度为2位小数的浮点数
# print("%s%d斤苹果，每斤%.2f元."%(sText1,n,fPrice))
# 我买了3斤苹果，每斤3.60元.

# ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#关键字（保留字）
# import keyword
# print(keyword.kwlist)

# iCount,sStudent,fPrice
# A9,_a344,U2_1
# 96667
# %Y3
# for,print
# MA U2
# l02 102 

#简单数据类型
# n = 3    #-22222   0,32
# print(n,type(n)) #integer整型  3 <class 'int'>
# f = 3.1415926
# print(f,type(f))  #float 浮点型  3.1415926 <class 'float'>
# s = 'Hello'
# print(s,type(s)) #string 字符串  Hello <class 'str'>
# b = 3 > 2
# print(b,type(b))   #boolean 布尔型 False True  True <class 'bool'>

# n = 0.14
# n = n * 100
# print(n) 
# if n == 14: #布尔表达式
#     print("0.14*100=14")
# else:
#     print("0.14*100<>14")  

# if n > 14 - 0.000001 and n < 14 + 0.000001:

# 缩进Tab
# python用严格的缩进来表示程序的结构

# 注意数据类型的变化
# a = 6
# b = 3.4
# c = a * b
# print(c,type(c))

# print(int(True)) 1
# print(int(False)) 0
# if 3: 
#     print('True')
# else:
#     print('False')
# if -0.00099: 
#     print('True')
# else:
#     print('False')
#
# 非零为真

#字符串 string '',"",'''  '''
# print('I told you,"Python is good."')
# print("I told you,'Python is good.'")
# print("I told you,\\\"Python is good.\"")

# #转义字符'\' 表示这个字符后面的那个字符原样输出
# \t 制表符 Tab  == 4 or 8 个空格
# \n 换行

# print("I know many languages as:\n\tJava\n\tPython\n\tC\n\tC++")
# sName = "alAn turning"
# print(sName.title())  Alan Turning
# print(sName.upper())  ALAN TURNING
# print(sName.lower())
# 面向对象程序设计
# 变量     == 对象 object
# 数据类型 == 类 class
#对象.方法()  对象.函数()

# sText = "     Hello World     "
# print("output by rstrip:",sText.rstrip(),'end')
# print("output by lstrip:",sText.lstrip(),'end')
# print("output by strip:",sText.strip(),'end')

#数据类型的转换
# s1 = "120s"
# s2 = "3.14159"
# i= int(s1)

# f = float(s2)
# s3 = str(i)
# s4 = str(f)
# print("i =",type(i),"f =",f,"s3 =",type(s3),"s4 =",s4)

# one=input()
# two=input()
# three=input()
# print(one+two+three,end=','),print("%.2f"%(float(one+two+three)/3))

# sname=[input().split(',')]
# smark=[input().split(',')]
# listfinal=[sname,smark]
# print(listfinal[0],listfinal[1])

# a,b,c=input().split(',')
# if float(a) >= float(b) and float(a) >= float(c):
#     print(a)
# elif float(b) >= float(a) and float(b) >= float(c):
#     print(b)
# elif float(c) >= float(a) and float(c) >= float(b):
#     print(c)

# fhua=float(input())
# cshe=float(5/9*(fhua-32))
# print("%.1f"%cshe)

# a,b,c,d=input().split(',')
# totalmark=float(a)+float(b)+float(c)+float(d)*0.7
# possible=(60-float(a)-float(b)-float(c))/0.7
# print("%.2f"%totalmark)
# print("%.2f"%possible)

# money = input()
# if money[0] in ['$']:

#     C = (eval(money[1:]))*6.78

#     print("&%.2f"%(C))

# elif money[0] in ['&']:

#     F = eval(money[1:])/6.78

#     print("$%.2f"%(F))

# elif money[0] in ['R']:

#     C1 = (eval(money[3:]))/6.78

#     print("USD%.2f"%(C1))

# elif money[0] in ['U']:

#     F2 = eval(money[3:])*6.78

#     print("RMB%.2f"%(F2))

# else:

#     print("Error")

# sums=input().split(',')
# sums2=eval(input())
# sums3=list(sums)
# sums4=()
# sums5=[]
# for i in range(len(sums3)):
#     sums4=(sums3[i],sums2[i])
#     sums5.append(list(sums4))
# print(sums5)


# def Fibonacci(num,n):
#     lastdo=0
#     first=1
#     second=1
#     if n <= 2:
#         lastdo=1
#     else:
#         for i in range(n-2):
#                 lastdo=first+second
#                 first=second
#                 second=lastdo
#     return lastdo

# num  =  [1,  1]
# n  =  int(input())
# print(Fibonacci(num,n))

# def search(nums):
#     sss=0
#     for i in nums:
#         if nums.count(i) > len(nums)//2:
#             sss=i
#         else:
#             sss="False"
#     return sss

# nums  =  eval(input())
# y  =  search(nums)
# print(y)

# n,m,l=eval(input())
# n,l=int(n),int(l)
# ls1=[x*n+ for x in range(1,m+1)]
# print(ls1)

# def rang(start,n,step):
#     start,n,step = int(start), int(n),int(step)
#     lst = [start]
#     while n > 1:
#         start,n = start+step,n-1     #注意这里的写法，习惯了c++，稍微有点不习惯，惊叹python的简洁
#         lst.append(start)
#     return lst

# n,m,l=eval(input())
# print(rang(n,m,l))

# dyh=eval(input())
# a,b=input().split(',')
# a=int(a)
# b=int(b)
# if a<len(dyh) and b<len(dyh):
#     if a<b:
#         del dyh[a:b]
#         print(dyh)
#     else:
#         del dyh[b:a:-1]
#         print(dyh)
# else:
#     print("error")

# nature=eval(input())
# sss=[]
# for i in nature:
#     if i == 2 or i == 3:
#         sss.append(i)
#     else:
#         k=0
#         for j in range(1,i+1):
#             if i % j == 0:
#                 k += 1
#         if k == 2:
#             sss.append(i)
# print(sss)

# dongxi=eval(input())
# average1=sum(dongxi)/len(dongxi)
# if average1-int(average1) == 0:
#     print(int(average1))
# else:
#     print("%.2f"%average1)

# dongxi=eval(input())
# average1=sum(dongxi)/len(dongxi)
# print("%.2f"%average1)

# ss=input().split(" ")
# a,b=input().split(" ")
# a=int(a)
# b=int(b)
# ss=list(ss)
# ss[a],ss[b]=ss[b],ss[a]
# print(ss)

# from os import remove

# lst=eval(input())
# a=min(lst)
# b=max(lst)
# while a in lst:
#     lst.remove(a)
# while b in lst:
#     lst.remove(b)
# print(lst)

# lst=eval(input())
# k=0
# for i in range(len(lst)):
#     while lst.count(i)>1:
#         lst.remove(i)
# print(lst)

# a=int(input())
# lst=[x for x in range(1,a+1)]
# lst2=[]
# for i in lst[1:]:
#        lst2.append(i)
# lst2.append(1) 
# print(lst2)


# lst=eval(input())
# lst.sort(reverse=True)
# sum=''
# for i in range(len(lst)):
#     sum += str(lst[i])
# print(int(sum))
        
# from collections import Counter

# lst=eval(input())
# counter=Counter(lst)
# result = [str(x) for x in counter if counter[x] == 1]
# if result:
#     result.sort()
#     c=",".join(result)
#     print(c)
# else:
#     print("False")


# from os import remove

# lst=eval(input())
# lst1=lst.copy()
# for x in lst1:
# 	if x==0:
# 		remove(x)
# 		lst.append(0)
# print(lst)

# lst=eval(input())
# a,b=input().split(",")
# lst=list(lst)
# a=int(a)
# b=int(b)
# if a<=len(lst):
#     c=lst[a]
#     for x in range(b):
#         lst.append(c)
#     print(lst)
# else:
#     print('error')



# lst=list(lst)
# pp=[lst[int(a)]]*int(b)
# c=",".join(pp)
# lst.append(pp)
# print(lst)




# a = [1,2,3,4,5,6,7]
# b = a
# c = a[0:]
# a[3:5] = 99,100
# print("a=",a,id(a)==id(b))
# print("b=",b)
# print("c=",c,id(c)==id(a))

# v1 = [x for x in range(-5,10,2)]
# v2 = "".join([chr(ord('a')+x)for x in range(26)])
# print("v1:",v1)
# print("v2:",v2)
# print(v1[0:5:])
# print(v1[-6:-1])
# print(v1[-1:-6:-2])
# print(v2[::])
# print(v2[::-5])
# print(v2[::-1])
# print(v2[:-5:7])

# print(list(range(4)))
# print(list(range(7,11)))
# print(list(range(1,14,3)))
# print(list(range(15,2,-4)))
# print(list(range(-20,20,4)))
# print(list(range(-1,-22,-7)))

# suits = ["红","梅","黑","方"] #四种花色
# ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] #13种牌面
# #将花色与牌面组合并加上大小王，生成54张牌的列表
# cards = [x+y for x in suits for y in ranks]
# print(cards)

# v = [7,11,13]
# print(max(v))
# print(min(v))
# print(sum(v))
# print("%.2f"%float(sum(v)/len(v)))

# fruits = ['grape','pear','apple','water melon']
# fruits.reverse()
# print("reversed fruits:",fruits)

# ss=eval(input())
# ss=list(ss)
# print(ss)


# def shift(lst):
#     lst = list1
#     list(lst)
#     list2=[]
#     list2.append(lst[-1])
#     for x in lst[:-1]:
#         list2.append(x)
#     lst == list2

# list1 = input().split(',')
# shift(list1)
# print(list1)



# def shift(lst):
#     lst = list1
#     a = lst.pop()
#     lst.insert(0,a)
#     return lst

# list1 = input().split(',')
# shift(list1)
# print(list1)

a=input()
b=input()
sd=[]
sd.append(a)
sd.append(b)
if sd[0]=="red":
    if sd[1]=="blue":
        print("purple")
    elif sd[1]=="yellow":
        print("orange")
    else:
        print("error")
elif sd[0]=="yellow":
    if sd[1]=="red":
        print("orange")
    elif sd[1]=="blue":
        print("green")
    else:
        print("error")
elif sd[0]=="blue":
    if sd[1]=="red":
        print("purple")
    elif sd[1]=="yellow":
        print("green")
    else:
        print("error")
else:
    print("error")


# a=input()
# b=input()
# if int(a)>0 and int(b)>0:
#     if int(a)==int(b):
#         print("It's a square")
#     else:
#         print("It's a rectangle")
# else:
#     print("illegal data")

# a=input()
# b=input()
# if int(a)>=99 and int(b)>=99:
#     print("You won a scholarship of 500 yuan!")
# elif int(a)<30 and int(b)<30:
#     print("You need to relearn!")

# a=input()
# if int(a)>=90:
#     print("A")
# elif 90>int(a)>=80:
#     print("B")
# elif 80>int(a)>=70:
#     print("C")
# elif 70>int(a)>=60:
#     print("D")
# else:
#     print("E")   

# a=input()
# b=[]
# for x in range(len(a)):
#     b.append(int(a[x]))
# for i in range(len(b)):
#     b[i] = (b[i] + 5) % 10
# b.reverse()
# for k in b:
#     print(k, end='')

# a=int(input())
# b=int(input())
# sums=a
# for x in range(b-1):
#     sums+=a*(0.5)**(x)
# print(sums)


# stu_list=[['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]
# xuehao=input()
# flag=False
# for x in range(len(stu_list)):
#     if stu_list[x][0]==xuehao:
#         flag=1
#         print(stu_list[x][0]+stu_list[x][1])
# if flag==0:
#     print("None")

# a=input()
# b=2
# c=1
# while a >0:
#     sums=2
#     sums+=b/c
#     x=c
#     c=b
#     b+=c
#     a-=1
# print("%.4f"%sums)

# sums=0
# n=0
# m=1
# while(m):
#     s=input()
#     if(s!="#"):
#         n+=1
#         sums+=int(s)
#     else:
#         m=0
# print(n,sums)





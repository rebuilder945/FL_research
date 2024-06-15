# #3
# def binary_search(stu_list, target):
#     left, right = 0, len(stu_list) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if stu_list[mid][0] == target:
#             return stu_list[mid]
#         elif stu_list[mid][0] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return None

# stu_list = [['201801','zhangyi'],['201802','zhanger'],['201803','zhangsan'],['201804','zhangsi'],
#             ['201805','wangyi'],['201806','wanger'],['201807','wangsan'],['201808','wangsi'],
#             ['201809','liyi'],['201810','lier'],['201811','lisan'],['201812','lisi'],
#             ['201813','zhaoyi'],['201814','zhaoer'],['201815','zhaosan'],['201816','zhaosi'],
#             ['201817','zhouyi'],['201818','zhouer'],['201819','zhousan'],['201820','zhousi']]

# target = input()
# result = binary_search(stu_list, target)
# if result:
#     print(result[0] + result[1])
# else:
#     print("None")
# #4 求和
# def    fibo(n):
#     if  n<=1:
#         return  1
#     elif n==2:
#         return  2
#     else:
#         return fibo(n-1)+fibo(n-2)

# n=int(input())
# lst1 = [fibo(x) for x in range(2,n+2)]    
# lst2 = [fibo(i) for i in range(1,n+1)]
# lst3 = [lst1[a]/lst2[a] for a in range(n)]
# S = sum(lst3)
# print("%.4f"%S)

# #5
# count = 0
# sum = 0

# while True:
#     num = input()
#     if num == '#':
#         break
#     num = int(num)
#     count += 1
#     sum += num

# print(count, sum)

# #6
# a = eval(input())
# if a <= 0 or type(a) == float:
#     print("illegal input")
# else:
#     lst=[]
#     for i in range(a):
#         b = str(i)
#         if b == b[::-1]:
#             lst.append(i)
#     s="2"
#     for x in lst[3:]:
#         c = 0
#         for y in range(2,x):
#             if x/y == x//y:
#                 c+=1
#         if c==0:
#             s+=" "+str(x)
#         else:
#             continue
#     print(s)

# #7
# n,m=map(int,input().split(" "))
# if n>0 and m>0 and m-n>=3 and n<10 and m<10:
#     lst1=[]
#     for x in range(n,m):
#         for y in range(n,m):
#             for z in range(n,m):
#                 if x!=y and x!=z and y!=z:
#                     lst1.append(x*100+y*10+z)
#     for i in lst1:
#         print(i,end=" ")
# elif n==0 and m>0 and m-n>=4 and n<10 and m<10:
#     lst1=[]
#     for x in range(n+1,m):
#         for y in range(n,m):
#             for z in range(n,m):
#                 if x!=y and x!=z and y!=z:
#                     lst1.append(x*100+y*10+z)
#     for i in lst1:
#         print(i,end=" ")
# else:
#     print("illegal input")

# #8
# a=input()
# b=input()
# if (a=='red' and b=='blue') or (b=='red' and a=='blue'):
#     print('purple')
# elif (a=='red' and b=='yellow') or (b=='red' and a=='yellow'):
#     print('orange')
# elif (a=='blue' and b=='yellow') or (b=='blue' and a=='yellow'):
#     print('green')
# else:
#     print('error')

# #9
# a=eval(input())
# if (a>=1 and a<=10) or (a>=19 and a<=28):
#     if a%2==0:
#         print('black')
#     else:
#         print('red')
# elif (a>=11 and a<=18) or (a>=29 and a<=36):
#     if a%2==0:
#         print("red")
#     else:
#         print('black')
# elif a==0:
#     print('green')
# else :
#     print("error")

# #10
# a=eval(input())
# if a>=3 and a<=5:
#     print('spring')
# elif a>=6 and a<=8:
#     print("summer")
# elif a>=9 and a<=11:
#     print("autumn")
# elif a==12 or a==1 or a==2:
#     print("winter")
# else:
#     print("error")


# #11
# lst1=list(input())
# shuzi=0
# zimu=0
# kongge=0
# qita=0
# for i in lst1:
#     if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
#         zimu+=1
#     elif ord(i)>=48 and ord(i)<=57:
#         shuzi+=1
#     elif i==' ':
#         kongge+=1
#     else:
#         qita+=1
# print("{} {} {} {}".format(zimu,kongge,shuzi,qita))

# #12
# def f(x):
#     if x<20:
#         return 6*x*x+1
#     elif x<40 and x>=20:
#         return (3*x-60)**(1/2)
#     elif x>=40:
#         return 100/(x+1)
# a=eval(input())
# eva=f(a)
# print("%.2f"%eva)

# #13
# amount = input().strip()

# if amount[0] in ('$','U'):
#     try:
#         if amount[0] == '$':
#             usd = float(amount[1:])
#             rmb = usd * 6.78
#             print('&{:.2f}'.format(rmb))
#         else:
#             usd = float(amount[3:])
#             rmb = usd * 6.78
#             print('RMB{:.2f}'.format(rmb))
#     except ValueError:
#         print('Error')
# elif amount[0] in ('&','R'):
#     try:
#         if amount[0] == '&':
#             rmb = float(amount[1:])
#             usd = rmb / 6.78
#             print('${:.2f}'.format(usd))
#         else:
#             rmb = float(amount[3:])
#             usd = rmb / 6.78
#             print('USD{:.2f}'.format(usd))
#     except ValueError:
#         print('Error')
# else:
#     print('Error')

# #14
# a=eval(input())
# b=eval(input())
# if a<=0 or b<=0:
#     print("illegal data")
# elif a==b:
#     print("It's a square")
# elif a!=b:
#     print("It's a rectangle")

# #15
# a=eval(input())
# b=eval(input())
# if a>=99 and b>=99:
#     print('You won a scholarship of 500 yuan!')
# elif a<30 and b<30:
#     print('You need to relearn!')

#16
lst1=input()
lst2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for x1 in lst2:
    jishu=0
    for x2 in lst1:
        if x1==x2:
            jishu+=1
    if jishu!=0:
        print("%c,%d"%(x1,jishu))

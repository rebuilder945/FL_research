# def  shift(lst):
#     a = lst[-1]
#     lst1 = lst.copy()
#     for i in range(len(lst)-1):
#         lst[i+1]=lst1[i]
#         lst[0]=a



# list1  =  input().split(",")  #输入格式  1,2,3,4,5
# shift(list1)
# print(list1)

# #2
# def  main():
#         N,M  =  map(int,input().split())
#         calculate_capital(N,M)
# def calculate_capital(a,b):
#     for i in range(b):
#         a = (1+0.003)*a
#     print%
# main()

# #3
# def  main():
#         total_count  =  int(input())
#         calculate_days(total_count)
# def calculate_days(a):
#     b = 0
#     while a>0:
#         b+=1
#         a=a-2-a//2
#     print(b)
#main()

# #4
# def  main():
#         a=int(input())
#         calculate_sum(a)
# def calculate_sum(x):
#     y = []
#     for i in range(1,x+1):
#         m = str(x)
#         z=eval(m*i)
#         y.append(z)
#     print(sum(y))    
# main()

# #5
# def  main():
#         num  =  eval(input())
#         calculate_e(num)
# def calculate_e(a):
#     e=0
#     for i in range(a+1):
#         n=1
#         for x in range(1,i+1):
#             n *=x
#         e+=1/n
#     print('%.6f'%e)
# main()

# #9 二月天
# def  leapyear(x):
#     if x%400 == 0:
#         return True
#     elif x%100!= 0 and x%4 ==0:
#         return True
#     else:
#         return False
      

# year=int(input())
# if  leapyear(year):
#         print("In  %d  February  has  29  days."%year)
# else:
#         print("In  %d  February  has  28  days."%year)

a =eval(input())
b =eval(input())
print(a,b)



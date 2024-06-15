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

#7
n,m=map(int,input().split(" "))
if n>0 and m>0 and m-n>=3 and n<10 and m<10:
    lst1=[]
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    lst1.append(x*100+y*10+z)
    for i in lst1:
        print(i,end=" ")
elif n==0 and m>0 and m-n>=4 and n<10 and m<10:
    lst1=[]
    for x in range(n+1,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    lst1.append(x*100+y*10+z)
    for i in lst1:
        print(i,end=" ")
else:
    print("illegal input")


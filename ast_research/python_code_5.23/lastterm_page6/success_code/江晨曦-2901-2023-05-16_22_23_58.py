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

#5
a=""
n = 0
lst = []
while a != "#":
    a =eval(input())
    n+=1
    lst.append(a)
print(n,sum(lst))

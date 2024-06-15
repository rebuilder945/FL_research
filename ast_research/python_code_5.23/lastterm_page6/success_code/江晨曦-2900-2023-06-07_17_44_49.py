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
# a=""
# n = 0
# lst = []
# while a != "#":
#     a =eval(input())
#     n+=1
#     lst.append(a)
# print(n,sum(lst))

#6
a = eval(input())
if a <0 or a ==float:
    print("illegal input")
else:
    lst=[]
    for i in range(a):
        b = str(i)
        if b == b[::-1]:
            lst.append(i)
    s="2"
    for x in lst[3:]:
        c = 0
        for y in range(2,x):
            if x/y == x//y:
                c+=1
        if c==0:
            s+=" "+str(x)
        else:
            continue
    print(s)


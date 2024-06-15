# n,m,l = eval(input())
# ls = [n+i*l for i in range(m)]
# print(ls)

# l = eval(input())
# n,m = eval(input())
# if n > len(l)-1 or m > len(l)-1:
#     print("error")
# else:
#     if n <= m:
#         del l[n:m]
#     else:
#         del l[n:m:-1]
#     print(l)

lst = eval(input())
n,m = eval(input())
if n > len(lst)-1:
    print("error")
else:
    del lst[n:m]
    print(lst)



# lst=eval(input())
# n,m=eval(input())
# if n<=m<(len(lst)-1):
#     for x in range (n,m):
#         del lst[x]
#     print(lst)
# else:
#     print("error")

# lst=eval(input())
# n,m=eval(input())
# lst1=lst.copy()
# if n<=m<=len(lst):
#     for i in lst[n:m]:
#         lst1.remove(i)
#     print(lst1)
# else:
#     print('error')

# lst=eval(input())
# n,m=eval(input())
# if n>len(lst)-1 or m >len(lst)-1:
#     print("error")
# else:
#     if n<=m:
#         del lst[n:m]
#     else:
#         del lst[n:m:-1]
# print(lst)


# lst=eval(input())
# n,m=eval(input())
# if n>len(lst)-1 or m >len(lst)-1:
#     print("error")
# else:
#     if n<=m:
#         del lst[n:m]
#     else:
#         n,m=m,n
#         del lst[n+1:m+1]
# print(lst)

lst=eval(input())
n,m=eval(input())
if  n>m or n>=(len(lst)) or m<=0 or m>len(lst):
    print('error')
else:
    print(lst[:n]+lst[m:])

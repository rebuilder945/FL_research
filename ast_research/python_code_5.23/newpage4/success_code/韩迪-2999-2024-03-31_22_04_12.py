a=list(input().split(" "))
n,m=map(int,input().split())
# b=input().split(" ")
# b=list(map(int,b))
# n=b[0]
# m=b[1]
# s=[]
# s.extend(a[0:n])
# s.extend(a[m])
# s.extend(a[n+1:m])
# s.extend(a[n])
# s.extend(a[m:])

# print(s)

# sTitle1=a.pop(n)
# sTitle2=a.pop(m-1)
# s=[]
# if n<m:
#     s.extend(a[0:n])
#     s.extend(sTitle1)
#     s.extend(a[n+1:m])
#     s.extend(sTitle2)
#     s.extend(a[m:])
#     print(s)
# else:
#     pass
# print(a[1])
# s=[]S
# for i in a:
#     if i!=n and i!=m:
#         s.extend(a(i))

#     else:
#         pass
# print(s)
a[n],a[m]=a[m],a[n]
print(a)

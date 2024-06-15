# #1
# a = input().split(',')
# b = eval(input())
# c = []
# for i in range(len(a)):
#     d = []
#     d.append(a[i])
#     d.append(b[i])
#     c.append(d)
# print(c)

# #2
# a,b,c = eval(input())
# lst = [x for x in range(a,a+b*c,c)]
# print(lst)

# #3
# a = eval(input())
# b,c = eval(input())
# if b<-len(a) or b>len(a)-1 or c<-len(a) or c>len(a)-1:
#     print("error")
# else:
#     if b<c-1:
#         del a[b,c-1]
#     elif b == c:
#         a=a
#     else:
#         del a[b]
#     print(a)

# #5
# a =eval(input())
# b = sum(a)/len(a)
# if b%1==0:

#     print(int(b))
# else:
#     print('%.2f'%b)

# #6
# a= eval(input())
# b = sum(a)/len(a)
# print('%.2f'%b)

# #7
# a= input().split()
# b,c =input().split()
# b = int(b)
# c = int(c)
# a[b],a[c]=a[c],a[b]
# print(a)

# #8
# a = eval(input())
# b = []
# m = max(a)
# n = min(a)
# for x in a:
#     if x in [n,m]:
#         continue
#     else:
#         b.append(x)
# print(b)

# #9
# a = eval(input())
# b = []
# a.reverse()
# for x in a:
#     if x in b:
#         continue
#     else:
#         b.append(x)
# b.reverse()
# print(b)

# #10
# n = eval(input())
# a = [x for x in range(1,n+1)]
# b = a[0]
# for i in range(n-1):
#     a[i]=a[i+1]
# a[-1] = b
# print(a)

# #11
# n = eval(input())
# n.sort(reverse = True)
# b=""
# for x in n:
#     b=b+str(x)
# if b[0] =="0":
#     print("0")
# else:
#     print(b)

# #12
# a = eval(input())
# b =[]
# for x in a:
#     if a.count(x)==1:
#         b.append(x)
#     else:
#         continue
# b.sort()
# if b ==[]:
#     print("False")
# else:
#     c=""
#     for i in b[0:-1]:
#         c+=str(i)+","
#     c+=str(b[-1])
 
#     print(c)

#13
a = eval(input())
b =[]
c =0
for i in a:
    if i == 0:
        c+=1
    else:
        b.append(i)
for x in range(c):
    b.append(0)
print(b)

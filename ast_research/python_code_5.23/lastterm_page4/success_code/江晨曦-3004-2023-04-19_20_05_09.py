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

#4
a = eval(input())
b = []
for x in a:
    if x ==2:
        b.append(2)
    else:
        d = 0
        for i in range(2,x):
            
            if x%i==0:
                d +=1
            else:
                continue
        if bool(d)==False:
            b.append(x)
        else:
            continue
print(b)
        


# a=eval(input())
# # b=[a.index(i) for i in a]
# # print(b)
# # for i in a:
# #     c=a.count(i)
# #     c=int(c)
# #     if c==1:
# #         print(i)
# #     else:
# #         print("False")
# for i in a:
#     b=[a.count(i) for i in a]
#     c=b.index(1)
# print(c)
a=eval(input())
b=[]
for i in range(len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
if len(b)!=0:
    b.sort(reverse=True)
    for i in range(len(b)-1):
        print(b.pop(),end=",")
    print(b.pop())
else:
    print("False")


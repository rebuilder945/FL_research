# 嵌套列表求和
# sum=0
# def sumlist(ls):
#     global sum
#     for i in ls:
#         if type(i)==int:
#             sum+=i
#         else:
#             sumlist(i)
# n=eval(input())
# sumlist(n)
# print(sum)

#加权求和
# """sum=0
# def sumlist(ls,level):
#     global sum
#     for i in ls :
#         if type(i)==int:
#             sum+=i*level
#         else:
#             sumlist(i,level+1)
#     return sum
# print(sumlist(eval(input()),1))"""

#身份验证
a=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
n=input()
if len(n)!=18:
    print("Error")
else:
    sum=0
    for i in range(17):
        sum+=a[i]*int(n[i])
    num=(12-sum%11)%11
    if num ==10:
        num="X"
    if num==n[-1] or num ==int(n[-1]):
        print("Correct")
    else:
        print("Wrong")
    

# a=eval(input())
# b=[]
# for n in a:
#     if n==1:
#         break
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 break
#             else:
#                 b.append(n)
# print(b)
def su(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
a=eval(input())
b=[]
for n in a:
    if su(n):
        b.append(n)
print(b)

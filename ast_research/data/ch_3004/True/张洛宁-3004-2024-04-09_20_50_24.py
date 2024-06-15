# a=eval(input())
# b=[]
# for n in a:
#     if n>=3 :
#         for i in range(2,n//2+1):
#             if n%1==0:
#                 b.append(n)
#     else:
#         a.remove(n)
# print(b)
def sushu(n):
    if n>=2 and type(n)==int:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    else:
        return False
a=eval(input())
b=[]
for x in a:
    if sushu(x)==True:
        b.append(x)
for c in b:
    if c==1 :
        b.remove(c)
print(b)


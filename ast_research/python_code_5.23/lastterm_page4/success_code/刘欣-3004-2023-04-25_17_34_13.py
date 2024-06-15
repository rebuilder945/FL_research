# def sushu(y):
#     x=[]
#     for i in y:
#         if i>=2:
#             for j in range(2,i,1):
#                 if i%j==0:
#                     break
#             else:
#                 x.append(i)
#     print(x)
# sums=eval(input())
# sushu(sums)

def sushu(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True
sums=eval(input())
x=[]
for i in sums:
    if sushu(i)==True:
        x.append(i)
print(x)

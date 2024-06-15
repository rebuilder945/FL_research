# n=eval(input())
# if n<=1 or n%1!=0:
#     print('illegal input')
# else:
#     for i in range(n+1):
#         if str(i)==str(i)[::-1]:  #字符串切片
#             for j in range(1,30):
#                 if i%j!=0:
#                     print(i)
#                 else:
#                     pass
#         else:
#             pass

def sushu(m):
    jishu=0
    for i in range(2,m):
        if m%i==0:
            jishu+=1
    if m==0 or m==1:
        return 1
    elif jishu==0:
        return 0
    elif jishu!=0:
        return 1
def huiwen(n):
    if str(n)[::-1]==str(n):
        return 0
    else:
        return 1
n=eval(input())
if n<=0 or type(n)==float:
    print("illegal input")
lst1=[]
for i in range(1,n):
    if sushu(i)==0 and huiwen(i)==0:
        lst1.append(i)
for i in lst1:
    print(i,end=' ')


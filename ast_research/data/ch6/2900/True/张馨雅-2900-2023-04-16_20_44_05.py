def sushu(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def huiwenshu(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=eval(input())
if n<2 or type(n)!=type(1):
    print('illegal input')
else:
    for i in range(2,n):
        if sushu(i) and huiwenshu(i):
            print(i,end=' ')

# count=0
# num=2
# Is=[]
# while count<n:
#     if sushu(num) and huiwenshu(num):
#         Is.append(num)
#         count+=1
#     num+=1
# for i in range(len(Is)):
#     if i %10!=0:
#         print('{:6}'.format(Is[1],end=' '))
#     else:
#         print()
#         print('{:6}'.format(Is[1],end=' '))

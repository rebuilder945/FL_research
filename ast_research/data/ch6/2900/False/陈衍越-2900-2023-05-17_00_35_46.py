def sushu(n):
    for i in range(2,n//2+1):
        if n%1==0:
            return 0
    return 1
def huiwenshu(n):
    if str(n)==str(n)[::-1]:
        return 1
    else:
        return 0
n=eval(input())
count=0
num=2
ls=[]
while count<n:
    if sushu(num) and huiwenshu(num):
        ls.append(num)
        count+=1
#print(ls)
for i in range(len(ls)):
    if i%10!=0:
        print('{:6}'.format(ls[i]),end='')
    else:
        print()
        print('{:6}'.format(ls[i]),end='')


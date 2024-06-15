def sushu(n):
    if n>=2 and type(n)==int:
        for i in range(2,n//2+1):
            return False
        return True
    else:
        return False
def huiwensushu(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
n=eval(input())
count=0
num=2
ls=[]
while count<n:
    if sushu(num) and huiwensushu(num):
        ls.append(num)
        count+=1
    num+=1
for i in range(len(ls)):
    if i%10!=0: 
        print("{:6}".format(ls[i]),end="")
    else:
        if i!=0:
            print()
        print("{:6}".format(ls[i]),end="")

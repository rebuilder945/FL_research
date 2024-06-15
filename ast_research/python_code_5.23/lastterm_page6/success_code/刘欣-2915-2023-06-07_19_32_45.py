def shuixian(n):
    s=0
    for nums in range(100,1000):
        nums=str(nums)
        for i in nums:
            i=int(i)
            s+=i**3
    if s==n:
        return True
    else:
        return False
n=int(input())
s=[]
if n <100 or n=="":
    print('none')
else:
    for i in range(100,n+1):
        if shuixian(i):
            s.append(i)
    if s==[]:
        print('none')
    else:
        for i in s:
            print(i,end=" ")


def nums(n):
    num=[x for x in range(1,n+1)]
    return num
def change(num):
    for i in range(n-1):
        num[i]=num[i+1]
    return num
n=eval(input())
num=nums(n)
result=change(num)
print(result)

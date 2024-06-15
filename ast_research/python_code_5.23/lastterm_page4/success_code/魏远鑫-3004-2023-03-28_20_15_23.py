result=[]
def sushu(n):
    for i in range(2,n//2+1):
        if n % i ==0:
             return False
    return True
list=eval(input())
if 1 in list:
    list.remove(1)
if 0 in list:
    list.remove(0)
for i in list:
   if sushu(i):
      result.append(i)
print(result)

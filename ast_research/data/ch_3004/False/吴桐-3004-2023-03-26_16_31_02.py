def sushu(num):
    if num==2:
        return num
    else:
        for i in range(2,num):
            if num%i==0:
                return False
            else:
                return num
lst=eval(input())
lst2=[]
for x in lst:
    n=sushu(x)
    if n==x:
        lst2.append(n)
    else:
        continue
print(lst2)


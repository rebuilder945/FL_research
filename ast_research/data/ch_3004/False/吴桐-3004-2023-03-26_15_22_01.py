def sushu(num):
    if num==2:
        return num
    else:
        for i in range(2,num):
            if num/i==0:
                return False
            else:
                return num
lst=list(eval(input()))
lst2=[]
for x in lst:
    n=sushu(x)
    lst2.append(n)
print(lst2)


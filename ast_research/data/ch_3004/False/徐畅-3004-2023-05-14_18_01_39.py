def sushu(n):
    a=0
    for x in range(2,n//2):
        
        if n%x==0:
            a=a+1
    if a==0:
            return 1
    else:
            return 0
lst=eval(input())
lst1=[]
for i in lst:
    if sushu(i)==1:
        lst1.append(i)
print(lst1)
        


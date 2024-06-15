lis=eval(input())
lst=[]
for i in range(len(lis)):
    n=int(list[i])
    for x in range(2,n):
        if n%x==0:
            break
        lst.append(n)
result=list(set(lis)-set(lst))            
print(result)

list=eval(input())
lst=[]
for i in range(len(list)):
    n=int(list[i])
    for x in range(2,n):
        if n%x==0:
            break
    lst.append(n)
result=list(set(list)-set(lst))            
print(result)

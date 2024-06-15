n=eval(input())
lst=[]

for x in range(1,n+1):
    lst.append(x)
    lst2=lst.copy()
for i in range(0,n+1):
    lst[i]=lst[i+1]
    if lst[i]==n:
        lst[i+1]=lst2[0]
        break
print(lst)



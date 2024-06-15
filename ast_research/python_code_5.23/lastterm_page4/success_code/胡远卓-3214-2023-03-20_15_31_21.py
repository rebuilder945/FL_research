lst=eval(input())
cnt=0
lst2=[]
for x in lst:
    if x==0:
        cnt+=1
    else:
        lst2.append(x)
for i in range(cnt):
    lst2.append(0)
print(lst2)

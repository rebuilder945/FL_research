n=eval(input())
lst=[]
count=0
for x in n:
    for i in range(2,x):
        if x%i==0:
            count+=1
    if count==0:
        lst.append(x)
print(lst)

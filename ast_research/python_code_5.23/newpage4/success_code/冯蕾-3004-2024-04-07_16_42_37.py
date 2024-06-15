lst=eval(input())
lst1=[]
def su(x):
    n=0
    for i in range(1,x):
        if x%i==0:
            n+=1
    if n==1:
        return True
for i in lst:
    if su(i):
        lst1.append(i)
print(lst1)




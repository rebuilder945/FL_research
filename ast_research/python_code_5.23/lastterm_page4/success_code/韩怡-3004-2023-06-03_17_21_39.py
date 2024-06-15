lst=eval(input())
lst2=[]
for n in lst:
    if n>=2:
        for i in range(2,n):
            if n%i != 0:
                lst2.append(i)
print(lst2)

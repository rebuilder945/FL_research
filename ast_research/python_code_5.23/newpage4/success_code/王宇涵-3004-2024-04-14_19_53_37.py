lst= eval(input())
lst1=[]
for x in lst:
    for i in range(2,x//2+1):
        if not x%i ==0:
           lst1.append(x)
print(lst1)

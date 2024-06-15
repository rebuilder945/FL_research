n=eval(input())
list1=[]
if n<1000:
    for x in range(100,n+1):
        if (x//100)**3+(x//10%10)**3+(x%10)**3==x:
            list1.append(x)
else:
    for x in range(100,1000):
        if (x//100)**3+(x//10%10)**3+(x%10)**3==x:
            list1.append(x)
if len(list1)==0:
    print("none")
else:
    for i in list1:
        print(i)

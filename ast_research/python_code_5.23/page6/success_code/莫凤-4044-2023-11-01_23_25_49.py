n=eval(input())
list1=[]
if n<1000:
    for x in range(100,n+1):
        a=x//100
        b=x%100//10
        c=x%10
        if a**3+b**3+c**3==x:
            list1.append(x)
else:
    for x in range(100,1000):
        a=x//100
        b=x%100//10
        c=x%10
        if a**3+b**3+c**3==x:
            list1.append(x)
if len(list1)==0:
    print("none")
else:
    for i in list1:
        print(i)

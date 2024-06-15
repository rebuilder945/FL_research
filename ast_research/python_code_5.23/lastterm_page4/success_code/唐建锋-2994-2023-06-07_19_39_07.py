list1=eval(input())
a,b=eval(input())
if a>=len(list1):
    print("error")
else:
    x1=list1[a]
    while b>0:
        list1.append(int(x1))
        b-=1
    print(list1)

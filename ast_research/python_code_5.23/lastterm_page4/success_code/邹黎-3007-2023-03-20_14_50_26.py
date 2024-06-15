list=eval(input())
a,b=eval(input())
if (len(list))>b and b>=a>=0:
    for x in range(a,b,1):
        del list[x]
    print(list)
else:
    print("error")



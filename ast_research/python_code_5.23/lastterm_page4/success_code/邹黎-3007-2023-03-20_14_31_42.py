list=eval(input())
a,b=eval(input())
if len(list)>=a+1 and len(list)>=b+1 and b>=a:
    for x in range(a-1,b-1):
        del list[x]
else:
    print("error")



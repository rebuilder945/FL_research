list=eval(input())
a,b=eval(input())
if len(list)>=b and b>=a:
    for x in range(a,b,1):
        del list[x-1]
        print(list)
else:
    print("error")



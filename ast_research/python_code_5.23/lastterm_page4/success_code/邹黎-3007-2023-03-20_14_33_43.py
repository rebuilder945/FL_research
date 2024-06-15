list=eval(input())
a,b=eval(input())
if len(list)>=b and b>=a:
    for x in range(a-1,b-1,1):
        del list[x]
        print(list)
else:
    print("error")



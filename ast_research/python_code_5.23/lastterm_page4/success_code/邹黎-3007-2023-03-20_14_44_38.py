list=eval(input())
a,b=eval(input())
if (len(list))>=b+1 and b>=a:
    for x in range(a,b,1):
        del list[x]
        print(list)
else:
    print("error")



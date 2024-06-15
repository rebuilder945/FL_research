list=eval(input())
a,b=eval(input())
if len(list)>a and len(list)>b and b>=a:
    for x in range(a-1,b-1):
        list.pop(list[x])
        print(list)
else:
    print("error")



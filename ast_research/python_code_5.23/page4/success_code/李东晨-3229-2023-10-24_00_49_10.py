a=eval(input())
for x in a:
    if a.count(x)==1:
        print(x,end=",")
if a.count(x)!=1:
    print("False")

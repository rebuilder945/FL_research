a=eval(input())
a.sort()
for i in a:
    number=a.count(i)
    if number==0:
        print("False")
    elif number==1:
        print(i,end="")

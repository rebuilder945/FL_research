num=int(input())
if list(range(1,11)).count(num)>=1:
    if num%2==0:
        print("black")
    else:
        print("red")
if list(range(19,29)).count(num)>=1:
    if num%2==0:
        print("black")
    else:
        pass
        print("red")
if list(range(11,19)).count(num)>=1:
    if num%2==1:
        print("black")
    else:
        pass
        print("red")
if list(range(29,37)).count(num)>=1:
    if num%2==1:
        print("black")
    else:
        pass
        print("red")
elif num==0:
    print("green")
else:
    pass
    print("error")

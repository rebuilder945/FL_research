a=eval(input())
if 0<=a<=36:
    if a==0:
        print("green")
    elif a in range(1,10,2) or  range(12,19,2) or range(19,28,2) or range(30,37,2):
        print("red")
    elif a in range(2,11,2) or range(20,29,2) or range(11,18,2) or range(29,36,2):
        print("black")
else:
    print("error")

a=eval(input())
if a==0:
    print("green")
elif a in list(range(1,11,2)) or a in list(range(12,19,2)) or a in list(range(19,29,2)) or a in list(range(30,37,2)):
    print("red")
elif a in list(range(2,11,2)) or a in list(range(11,19,2)) or a in list(range(20,29,2)) or a in list(range(29,37,2)):
    print("black")
else:
    print("error")


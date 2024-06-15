a = eval(input())
if a in range(1,10,2) or a in range(12,19,2) or a in range(19,28,2) or a in range(30,37,2):
    print("red")
elif a in range(2,11,2) or a in range(11,18,2) or a in range(20,29,2) or a in range(29,36,2):
    print("black")
elif a == 0:
    print("green")
else:
    print("error")
    

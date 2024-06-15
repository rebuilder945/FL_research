a = eval(input())
b = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
if a in range(37):
    if a == 0:
        print("green")
    elif a in b:
        print("red")
    else:
        print("black")
if a not in range(37):
    print("error")

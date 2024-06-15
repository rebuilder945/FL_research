yuan1 = input()
yuan2 = input()
pc = ["red","blue","yellow"]
red = r
blue = b
yellow = y
if yuan1 not in pc or yuan2 not in pc or yuan1 == yuan2:
    print("error")
else:
    if yuan1 == r and yuan2 == b:
        print("purple")
    elif yuan1 == r and yuan2 == y:
        print("orange")
    elif yuan1 == b and yuan2 == y:
        print("green")
    elif yuan1 == b and yuan2 == r:
        print("green")
    elif yuan1 == y and yuan2 == r:
        print("orange")
    elif yuan1 == y and yuan2 == b:
        print("green")



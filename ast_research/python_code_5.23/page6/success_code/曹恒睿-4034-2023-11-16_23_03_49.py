n1 = input()
n2 = input()
panduan = ["red","yellow","blue"]
if n1 not in panduan or n2 not in panduan:
    print("error")
else:
    if n1 == n2:
        print("error")
    elif n1 == "red" and n2 == "yellow" or n2 == "red" and n1=="yellow":
        print("orange")
    elif n1 == "red" and n2 == "blue" or n2 == "red" and n1 =="blue":
        print("purple")
    elif n1 == "yellow" and n2 == "blue" or n1 == "blue" and n2 == "yellow":
        print("green")

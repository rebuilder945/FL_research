yuanse1 = input()
yuanse2 = input()
if yuanse1 == "red" and yuanse2 == "blue":
    print("purple")
if yuanse1 == "red" and yuanse2 == "yellow":
    print("orange")
if yuanse1 == "blue" and yuanse2 == "yellow":
    print("green")
if yuanse1 and yuanse2 not in ["red","blue","yellow"]:
    print("error")
if yuanse1 == yuanse2:
    print("error")

m=input()
n=input()
yuan=["red","blue","yellow"]
if m not in yuan or n not in yuan or m==n:
    print("error")
if m in ["red","blue"] and n in ["red","blue"]:
    print("purple")
if m in["red","yelllow"] and n in ["red","yellow"]:
    print("orange")
if m in ["blue","yellow"] and n in["bule","yellow"]:
    print("green")

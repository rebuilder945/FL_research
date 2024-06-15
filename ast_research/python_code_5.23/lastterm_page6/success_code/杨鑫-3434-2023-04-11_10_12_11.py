p1 = input()
p2 = input()
if p1 == p2 or p1 not in ["red","blue","yelllow"] or p2 not in ["red","blue","yellow"]:
    print("error")
elif p1 in ["red","blue"] and p2 in ["red","blue"]:
    print("purple")
elif p1 in ["red","yellow"] and p2 in ["red","yellow"]:
    print("orange")
elif p1 in ["blue","yellow"] and p2 in ["blue","yellow"]:
    print("green")

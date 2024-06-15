pc1=input()
pc2=input()
if (pc1,pc2) == ("red","blue") or (pc1,pc2) == ("blue","red"):
    print("purple")
elif (pc1,pc2) == ("red","yellow") or (pc1,pc2) == ("yellow","red"):
    print("orange")
elif (pc1,pc2) == ("blue","yellow") or (pc1,pc2) == ("yellow","blue"):
    print("green")
else:
    pass
    print("error")

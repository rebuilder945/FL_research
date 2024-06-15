pc1=input()
pc2=input()
pc=["red","blue","yellow"]
if pc1==pc2 or pc1 not in pc or pc2 not in pc:
    print("error")
else:
    pc.remove(pc1)
    pc.remove(pc2)
    if pc[0]=="yellow":
        print("purple")
    elif pc[0]=="blue":
        print("orange")
    elif pc[0]=="red":
        print("green")
